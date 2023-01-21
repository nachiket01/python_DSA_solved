str = "SAAAAS"
mid = int(len(str)/2)

end = int(len(str))
end -=1 

for i in range(mid):
    if str[i] != str[end]:
        print("not palindrome")
        end-=1
    
    if str[i] == str[end]:
        print("given string is palindrome \n first",str[i],"last",str[end])
        
