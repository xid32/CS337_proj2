from get_tools import TOOLS
from fetchURL import fetchURL
from parse import findDirection
import re
import json


def get_directions():
    fetchURL('https://www.allrecipes.com/recipe/270363/guinness-cupcakes-with-espresso-frosting/')
    f = open("url.txt", "r")
    s = f.read()
    dirs = findDirection(s)["recipeInstructions"]

    dirs_rep = []
    for dir in dirs:
        text = dir["text"]
        dir_rep = {}
        dir_rep["full_text_direction"] = text
        dir_rep["tools"] = find_tools(text)
        dir_rep["time"] = find_time(text)
        dirs_rep.append(dir_rep)
    return dirs_rep
    

def find_tools(text):
    tools_for_this_step = []
    for TOOL in TOOLS:
        if TOOL in text:
            tools_for_this_step.append(TOOL)
    return tools_for_this_step


# TODO: Remove Overlap time
def find_time(text):

    # Rules:
    hour_minute = re.findall(r"[0-9]+ hour and [0-9]+ minute", text)
    minute_second = re.findall(r"minute and [0-9]+ second", text)

    # Probably don't need hour_second and hour_minute_second since they are too specific
    second = re.findall(r" [0-9]+ second", text)
    minute = re.findall(r" [0-9]+ minute", text)
    hour = re.findall(r" [0-9]+ hour", text)


    rules = [hour_minute, minute_second, second, minute, hour]
    time = {}
    for rule in rules:
        for item in rule:
            ind = text.find(item)
            while ind in time and ind < len(text):
                oldind = ind
                ind = text[oldind+len(item):].find(item)
                ind = oldind + len(item) + ind
            time[ind] = item
    # new_time_dict = dict(sorted(time.items(), key=lambda item: item[1]))
    # return new_time_dict
    return remove_overlap_time(time)

def remove_overlap_time(time_dict):
    interval = []
    for ind in time_dict:
        if is_compound_time(time_dict[ind]):
            start = ind
            end = start + len(time_dict[ind])
            interval.append((start, end))

    for ind in time_dict:
        if not is_compound_time(time_dict[ind]):
            start = ind
            if is_overlap(start, interval):
                time_dict[ind] = "removed"
    return time_dict

def is_compound_time(time):
    return ("hour" in time and "minute" in time) or ("minute" in time and "second" in time) 
    
def is_overlap(start, interval):
    for tup in interval:
        if tup[0] <= start + 1 and start + 1 <= tup[1]: return True
    return False

print(json.dumps(get_directions(), indent=4, sort_keys=True))
print(find_time("heat for 5 hour and 15 minute, boil for 5 minute, wait 5 minute to cool"))
print(find_time("5 hour, 5 hour, 5 hour, 5 hour, heat for 5 hour and 15 minute, boil for 5 minute, wait 5 minute to cool"))
