def strfind(main_str,search_str,dir='f'):
    k=0
    if(dir=='f'):
      for i in main_str:
        k=k+1
        if(i==search_str):
            print(k)

    else  :
       for i in reversed(main_str):
          k=k+1
          if(i==search_str):
             print(k)
    # print(main_str.index(search_str))

strfind("Hello",'o','f')