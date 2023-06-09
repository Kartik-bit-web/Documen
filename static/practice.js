today = new Date();
currentMonth = today.getMonth();
currentYear = today.getFullYear();

selectYear = document.getElementById("year");
selectMonth = document.getElementById("month");

const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

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

    firstdate = new Date(year, month).getDay()-1;
    tbl.innerHTML = "";
    tbl.innerHTML = '<thead> <tr><th scope="col">Mon</th><th scope="col">Tue</th><th scope="col">Wed</th><th scope="col">Ths</th><th scope="col">Fri</th><th scope="col">Sat</th><th scope="col">Sun</th></tr> </thead>'

    selectMonth.innerHTML = months[month]
    selectYear.innerHTML = currentYear
    tbody = document.createElement('tbody')
    date = 1;
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
                td.style.cursor = 'pointer';

                alink = document.createElement('a')
                att2 = document.createAttribute('id')
                att2.value =`${date}${month}${year}`
                alink.setAttributeNode(att2)

                att = document.createAttribute('href')
                att.value = " /admin_main/create_event"
                alink.setAttributeNode(att)
                      
                tdText = document.createTextNode(date)
                if (today.getDate() == date && today.getFullYear() == year && today.getMonth() == month){
                    alink.appendChild(tdText)
                    td.appendChild(alink)
                    tr.appendChild(td)
                    date++
                }
                
                else{
                    alink.appendChild(tdText)
                    td.appendChild(alink)
                    tr.appendChild(td)
                    date++

                }
                
                 
            }
        }
        tbl.appendChild(tbody)
        tbody.appendChild(tr)
        
    }
}

function daysInMonth(iMonth, iyear){
    return 32 - new Date(iMonth, iyear, 32).getDate();
}


console.log('hello')

