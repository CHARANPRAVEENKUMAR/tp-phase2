import streamlit as st 
from PIL import Image
img = Image.open("flamesImage.jpeg")
st.image(img,width=340)
col1,col2=st.columns(2)
col1.title("Welcome to the Flames game")
col2.image("fire-flames.jpg",width=100)
boy=st.text_input("Enter the Boy Name")
girl=st.text_input("Enter the Girl Name")
boy=list(boy)
girl=list(girl)
# boy=list(input("Enter nibba name:").strip())
# girl=list(input("Enter nibbi name:").strip())
for i in range(len(boy)):
    for j in range(len(girl)):
        if boy[i] == girl[j]:
            boy[i]=girl[j]='9'
            break 
nonDuplicate=boy+girl
count=0
# print(boy,girl)
for i in nonDuplicate:
    if i !='9':
        count+=1
# print(count)
result=['Friends','Lovers','Affectionate','Marriage','Enemies','Siblings']
j=0
while(len(result)>1):
    newval=count
    while newval>len(result):
        newval-=len(result)
    # print("count",count,result,newval)
    result.pop(newval-1)
print(result)
if st.button('submit'):
    if len(boy)!=0 and len(girl)!=0:
        st.success("relation between "+result[0])
    elif len(boy)==0:
        st.error("respected Boy name is missing")
    elif len(girl)==0:
        st.error("respected Girl name is missing")
        