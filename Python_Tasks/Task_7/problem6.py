s = input().lower()

if set("abcdefghijklmnopqrstuvwxyz").issubset(set(s)):
    print("pangram")
else:
    print("not pangram")
    
