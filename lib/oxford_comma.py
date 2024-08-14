def oxford_comma(items):
    if len(items) == 1:
        return "".join(items)
    
    elif len(items) == 2:
        join_two= " and ".join(items)  
        return join_two
    
    elif len(items) == 3:
        join_first_items = ", ".join(items[:2])
        all_together = f"{join_first_items}, and {items[2]}"
        return all_together
    
    elif len(items) > 3:
        last_item = len(items) - 1
        join_first_items = ", ".join(items[:last_item])
        all_together = f"{join_first_items}, and {items[last_item]}"
        return all_together

oxford_comma(["fiddleheads", "okra", "kohlrabi"])