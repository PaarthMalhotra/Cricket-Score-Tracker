from fastapi import FastAPI,Form
from fastapi.responses import FileResponse,HTMLResponse,RedirectResponse
from data import insert_match_Details, Identify_Over, update_score_inning1,update_score_inning2,get_id

app = FastAPI()

@app.get("/")
def home():
    return FileResponse('home_page.html')

@app.get("/new")
def new_page():
    return FileResponse('new_match.html')

@app.get("/past-records")
def past_records_page():
    return {"message": "These are the past records!"}

@app.post("/inning_count")
def handle_form(team1: str = Form(...), team2: str = Form(...), format: str = Form(...)):

    T_over = Identify_Over(format)
    value = (team1,team2,format,T_over)
    insert_match_Details(value)
    return RedirectResponse('/inning_1',status_code=303)

@app.get("/inning_1")
def count():
    return FileResponse('inning_1.html')

@app.post("/update_ball_1")
def updating(ball_count:int  = Form(...), runs:int = Form(...),out:str = Form(...)):
    match_id = get_id()
    if ball_count != 6:
        update_score_inning1(runs,match_id)
        return FileResponse('inning_1.html')
    elif ball_count == 6:
        update_score_inning1(runs,match_id)
        return RedirectResponse('/inning_2',status_code=303)


@app.get("/inning_2")
def count():
    return FileResponse('inning_2.html') 


@app.post("/update_ball_2")
def updating(ball_count:int  = Form(...), runs:int = Form(...),out:str = Form(...)):
    match_id = get_id() 
    if ball_count != 6:
        update_score_inning2(runs,match_id)
        return FileResponse('inning_2.html')
    elif ball_count == 6:
        update_score_inning2(runs,match_id)
        return FileResponse('thankyou.html')




