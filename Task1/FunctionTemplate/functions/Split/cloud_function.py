def cloud_function(json_input):
    Text = json_input["TextStr"]
    W = json_input["Wnum"]   
    Text_list = list(Text.split(" ")) 
    splitted_Text= lambda list, x: [list[i:i+x] for i in range(0, len(list), x)]
    result = splitted_Text(Text_list,W)
    # return the result
    res = {
        "BatchArr": result
    }
    return res
