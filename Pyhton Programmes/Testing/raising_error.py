def validate_username(name, max):
    assert type(name) == str, " username must be string"
    if max < 1:
        raise ValueError("minlen must be atleast 1")
    if not name.isalnum():
        return False
    if len(name)>max:
        return False
    
    return True
print(validate_username(["a"], -1))

