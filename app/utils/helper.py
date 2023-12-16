def find_item_in_list(list, cb):
    for index, item in enumerate(list):
        if cb(item, index, list):
            return item



items = [
    {"name":"ada", 'email':"adatest@gmail.com"},
    {"name":"obi", 'email':"obitest@gmail.com"},
    {"name":"john", 'email':"johntest@gmail.com"},
    {"name":"mark", 'email':"marktest@gmail.com"}
]
#get the item where
#1 name = obi
#2 email = market.com
#3 name = jace -> none
def get_name_obi(value, index, array):
    # print("value", value,  "Index:", index, "array: ", array, "\n\n")
    return value.get("name") == "obi"


def get_email(value, index, array):
    return value.get("email") == "mark@test.com"
# oor

res = find_item_in_list(items, lambda value, *rest: value.get("email") == "marktest@gmail.com")


def get_name_jace(value, index, array):
    # print("value", value,  "Index:", index, "array: ", array, "\n\n")
    return value.get("name") == "jace"

print(find_item_in_list(items, get_name_obi))
print(find_item_in_list(items, get_name_jace))
print(find_item_in_list(items, get_email))