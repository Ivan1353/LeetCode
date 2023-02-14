def lengthOfLongestSubstring(s):
    list_string = list(s)
    curr_list = []
    max_len = 0
    for i in list_string:
        if i not in curr_list:
            curr_list.append(i)
        else:
            curr_list = [i]
        if len(curr_list) > max_len:
            max_len = len(curr_list)
    return max_len