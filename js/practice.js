today = new Date();
currentMonth = today.getMonth();
currentYear = today.getFullYear();
selectYear = document.getElementById("year");
selectMonth = document.getElementById("month");

showCalendar(currentMonth, currentYear);

tbl = document.getElementById('tbl')

function next(){
    currentYear = currentMonth === 11 ? currentYear +1: currentYear;
    currentMonth = (currentMonth + 1)% 12;
    showCalendar(currentMonth, currentYear)
}

function prev(){
    currentYear = currentMonth === 0 ? currentYear -1: currentYear;
    currentMonth = (currentMonth === 0)? 11: currentMonth -1 ;
    showCalendar(currentMonth, currentYear)
}

function showCalendar(month, year){

    firstdate = new Date(year, month).getDay()-1
    tbl.innerHTML = "";
    tbl.innerHTML = '<tr><th>Mon</th><th>Tue</th><th>Wed</th><th>Ths</th><th>Fri</th><th>Sat</th><th>Sun</th></tr>'

    date = 1
    for(i=0; i < 6; i++){
        tr = document.createElement('tr');
        for(j=0; j< 7; j++){
            if(i==0 && j< firstdate){
                td = document.createElement('td');
                tdText = document.createTextNode('')
                td.appendChild(tdText)
                tr.appendChild(td)
            }
    
            else if(date > daysInMonth(year, month)){
                break;
            }
    
            else{
                td = document.createElement('td');
                tdText = document.createTextNode(date)
                td.appendChild(tdText)
                tr.appendChild(td)
                date++
            }
        }
        tbl.appendChild(tr)
    }
}

function daysInMonth(iMonth, iyear){
    return 32 - new Date(iMonth, iyear, 32).getDate();
}
