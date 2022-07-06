
import sqlite3 as sql
import speech_recognition as sr
import pyttsx3
import datetime
from func import *
import func as func_library
import easygui


def unique(list1):
    unique_list = []

# traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    return unique_list

result_of_talk_array=[]
final_results = []
sumition = 0
result=""
get_feeling_tube=[]
speed=150

no_of_min_of_duration_of_symp=.1


     

    


def jeckvoice(text):


    # Import the required module for text
	# to speech conversion

	# init function to get an engine instance for the speech synthesis
    engine = pyttsx3.init()
    engine.setProperty("rate", speed)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    # say method on the engine that passing input text to be spoken
    engine.say("{}".format(text))

    # run and wait method, it processes the voice commands.
    engine.runAndWait()
    return 0

# Function to convert text to
sql_db_link="C:\\Users\\ahmed\\Desktop\\programming\\drug simulator sinai\\models\\model 4\\programming\\jack db.db"

choices_array_final = ["talk slower please","talk faster please","show me the symptoms that you feel"]
if __name__=="__main__":
    #while using microphone
    while 1 :

       
                #if order of disease
    #------------------------------------------------------------------
        con = sql.connect("{}".format(sql_db_link))
        cur = con.cursor()
        
        get_choices = cur.execute("SELECT question FROM quistions_db")
        for get_choices_result in get_choices:
            
            choices_array_final.append(get_choices_result[0])

        get_choices2 = cur.execute("SELECT effector,type_effector FROM blocks")
        for get_choices_result2 in get_choices2.fetchall():
            if "{}".format(get_choices_result2[1]) == "drug":
                text = "take {} {}".format("{}".format(
                    get_choices_result2[1]), "{}".format(get_choices_result2[0]))
                choices_array_final.append(text)
            if "{}".format(get_choices_result2[1]) == "disease":
                text = "make {} {}".format("{}".format(
                    get_choices_result2[1]), "{}".format(get_choices_result2[0]))
                choices_array_final.append(text)
       
        #what he real feel
       
        get_feel = cur.execute(
            "SELECT nameofsymp FROM quistions_db WHERE activate_state='a' ")
        for get_feel_result in get_feel.fetchall():
            get_feeling_tube.append(get_feel_result[0])
        print([i for i in get_feeling_tube])
            
            
        if len(get_feeling_tube)==0:
            
            result = easygui.choicebox(choices=unique(choices_array_final),msg="what i feel : {}".format("no clinical issues i think"))
            
        if len(get_feeling_tube) > 0:
            
            result = easygui.choicebox(choices=unique(
                choices_array_final), msg="what i feel : {}".format([i for i in get_feeling_tube]))
        
        if result=="talk slower please":
            speed=speed-50
        if result == "talk faster please":
            speed = speed + 50

        result_of_talk_array.clear()
        get_feeling_tube.clear()
        result_of_talk_array.append("{}".format(result))
        #status asking 
        get_status = cur.execute(
            "SELECT answer FROM quistions_db WHERE nameofsymp='status' and question='{}'  ".format(result))
        for status_result in get_status.fetchall():
            if len(status_result)!= 0 :  
                jeckvoice("{}".format(status_result[0]))
       
       
#--------------------------------------------------------------------------------
       
        #show symptoms
        if "show me the symptoms that you feel" in result_of_talk_array[0]:
            physics_symp_arr=[]
            import sqlite3 as sql
            con_res = sql.connect("{}".format(sql_db_link))
            cur_res = con_res.cursor()
        
            c1=cur_res.execute("SELECT nameofsymp,state,place FROM quistions_db WHERE activate_state='a' ")
            rows=c1.fetchall()
            
            for r in rows:
                physics_symp_arr.append(r)
            
            if len(physics_symp_arr) != 0 :
                import time
                start_time = time.time()

                seconds = int(no_of_min_of_duration_of_symp*60)

                while True:
                    current_time = time.time()
                    elapsed_time = current_time - start_time
                    
                    if elapsed_time > seconds:
                        print("Finished iterating in: " + str(int(elapsed_time)) + " seconds")
                        break
                # make the physic symp here
                make_func_automatic(physics_symp_arr)
            
            if len(physics_symp_arr) == 0 :
                import time
                start_time = time.time()

                seconds = int(no_of_min_of_duration_of_symp*60)

                while True:
                    current_time = time.time()
                    elapsed_time = current_time - start_time
                    
                    if elapsed_time > seconds:
                        print("Finished iterating in: " +
                              str(int(elapsed_time)) + " seconds")
                        break
                
                    #make normal symp 
                    func_library.normal().make_all()



        #continue ----------->------------------------------------------------
           

        ##make a disease
        if "make disease" in result_of_talk_array[0]:
            
            final_text = result_of_talk_array[0].split()
            final_text.remove("make")
            final_text.remove("disease")
           
            results = cur.execute("SELECT nameofsymp,state,place FROM blocks WHERE effector='{}' ".format("{}".format(final_text[0])))
            for res in results.fetchall():

    
                result = cur.execute(" UPDATE quistions_db SET activate_state='{}', place='{}'  WHERE nameofsymp='{}' and state='{}' ".format(
                    "a", "{}".format(res[2]), "{}".format(res[0]), "{}".format(res[1])))
                con.commit()
        # if ask a question : 
        final_results = []
        sumition = 0
        results6 = cur.execute("SELECT question FROM quistions_db")
        questions_tube = []
        for res6 in results6.fetchall():
            questions_tube.append(res6[0])

        
        final_data = unique(questions_tube)
        if result_of_talk_array[0] in final_data:

            results7 = cur.execute(
                "SELECT answer,activate_state FROM quistions_db WHERE question='{}'  ".format("{}".format(result_of_talk_array[0])))
            compare_tube = []
            for res7 in results7.fetchall():

                compare_tube.append(res7)
            n = 0
            
            count = 0

            #ttt tube

            for comp in compare_tube:
                count=count+1
                print(n)

                if comp[1] == "n":
                    n = n+1
               
                if n == 3:
                    results8 = cur.execute(
                        "SELECT answer,place FROM quistions_db WHERE question='{}' and state='0'  ".format("{}".format(result_of_talk_array[0])))
                    for res8 in results8.fetchall():
                            if " ((organ))" in res8[0]:
                                    jeckvoice("{}".format(res8[0]).replace(
                                        "((organ))", "{}".format(res8[1])))
                            else:
                                jeckvoice(("{}".format(res8[0])))
                    break
                
                 
            if n < 3: 
                #if 1
                results9 = cur.execute(
                    "SELECT answer,state,place FROM quistions_db WHERE question='{}' and activate_state='a'   ".format("{}".format(result_of_talk_array[0])))
                for res9 in results9.fetchall():
                    print(res9[0])
                    print(count)
                    
                            
                    if "((organ))" in res9[0]:
                            jeckvoice("{}".format(res9[0]).replace("((organ))", "{}".format(res9[2])))
                    if "((organ))" not in res9[0]:
                            jeckvoice(("{}".format(res9[0])))
                    break
        

                
            
        # ---------------- > end 
        ##give a drug
        if "take drug" in result_of_talk_array[0]:

            final_text = result_of_talk_array[0].split()
            final_text.remove("take")
            final_text.remove("drug")
            jeckvoice("ok doctor thanks ..... i will take {} ............and tell you what habbened".format(final_text[0]))
            con2 = sql.connect(
                "{}".format(sql_db_link))
            cur2 = con2.cursor()
                           
            # here we activated the 2 probability now we compare
            results3 = cur2.execute(
                "SELECT * FROM quistions_db WHERE activate_state='a'  ")
            for res3 in results3.fetchall():
                results4 = cur.execute(
                    "SELECT state FROM quistions_db WHERE activate_state='a' and nameofsymp='{}'   ".format(res3[0]))
                for res4 in results4.fetchall():
                    results2 = cur2.execute("SELECT state FROM blocks WHERE effector='{}'and nameofsymp='{}' ".format(
                        "{}".format(final_text[0]), "{}".format(res3[0])))
                    for res2 in results2.fetchall():


                        sumition = int(res4[0]) + int(res2[0])
                        

                final_results.append([res3[0], sumition])
                sumition = 0
   
            for change_state in final_results:
                if change_state[1]==0:
                    result5 = cur.execute(" UPDATE quistions_db SET activate_state='{}', place='{}'  WHERE nameofsymp='{}' and state='{}' or state='{}' ".format(
                        "n", "n", "{}".format(change_state[0]), "1", "-1"))
                    con.commit()

## for now its make disease and give a treatement






    
    


def install_pips():
    #install these lib
    #pip install pipwin
    #pipwin install pyaudio
    #pip install sklearn
    # pip install numpy
    #pip install speech_recognition as sr
    #pip install pyttsx3
    #pip install  easygui

    return 0
