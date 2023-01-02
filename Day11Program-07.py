#nested dictionary
sampleDict={
    "class":{
        "student":{
            "name":"Mike",
            "marks":{
                "Physics":70,
                "history":80,
            }
        }
    }
}
print(sampleDict['class']['student']['marks']['history'])         
