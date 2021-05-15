

async function show(){
    console.log("got")
    var data= await fetch('http://192.168.1.6:7000/showtable').then(res => res.json()).then(data=> { return data});
    var table=document.getElementById("table");
    var row = table.insertRow();
    var cell1 = row.insertCell()
    var cell2 = row.insertCell()
    var cell3 = row.insertCell()
    var cell4 = row.insertCell()
    var cell5 = row.insertCell()
    var cell6 = row.insertCell()
    cell1.innerHTML = "<b>Full Name</b>";
    cell2.innerHTML = "<b>Roll Number</b>";
    cell3.innerHTML = "<b>Maths</b>";
    cell4.innerHTML = "<b>Physics</b>";
    cell5.innerHTML = "<b>Chemistry</b>";
    cell6.innerHTML = "<b>Biology</b>";
    for(i of data){
            var row = table.insertRow();
            var cell1 = row.insertCell()
            var cell2 = row.insertCell()
            var cell3 = row.insertCell()
            var cell4 = row.insertCell()
            var cell5 = row.insertCell()
            var cell6 = row.insertCell()
            cell1.innerHTML = i[0];
            cell2.innerHTML = i[1];
            cell3.innerHTML = i[2];
            cell4.innerHTML = i[3];
            cell5.innerHTML = i[4];
            cell6.innerHTML = i[5];
        }
    }

