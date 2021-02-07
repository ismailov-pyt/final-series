from ozgar import*
while True:
    print('Durrang 1 tadan imkoniyat!!!')
    kompyuter=randrange(1,4)

  

    print("Qayerga tepasiz? \n1)O`nga\n2)O`rtaga\n3)Chapga")
    user=int(input('Belgini kiriting(1,2,3)>>> '))
    if kompyuter==1:
       print(f'\n\n\n{k} {a} ga otildi;))')
    if kompyuter==2:
       print(f'\n\n\n{k}  {b} ga otildi;))')
    if kompyuter==3:
       print(f'\n\n\n{k}  {c} ga otildi;))')
    if kompyuter==user:
       print(f"//{k}  to'sdi, {siz} |{us}:{komp}| {k} //")
    if kompyuter!=user:

        us+=1
        print(f"//GOOOOOL, {siz} |{us}:{komp}|  {k} //") 

    kompyuter=randrange(1,4)

  

    print("Qayerga otilasiz? \n1)O`nga\n2)O`rtaga\n3)Chapga")
    user=int(input('Belgini kiriting(1,2,3)>>> '))
    if kompyuter==1:
       print(f'\n\n\n{k} {a} ga tepdi;))')
    if kompyuter==2: 
        print(f'\n\n\n{k}  {b} ga tepdi;))')
    if kompyuter==3:
       print(f'\n\n\n{k}  {c} ga tepdi;))')
    if kompyuter==user:
       print(f"//siz  to'sdingiz, {siz} |{us}:{komp}| {k} //")
    if kompyuter!=user:

       komp+=1
       print(f"//GOOOOOL, {siz} |{us}:{komp}| {k} //")
    if komp!=us:
        break