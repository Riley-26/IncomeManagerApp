const mainModal = document.getElementsByClassName("modal")[0];
const incomeForm = document.getElementsByClassName("income-form")[0];
const expenseForm = document.getElementsByClassName("expense-form")[0];
document.getElementById("main").onload = () => loadElements();

function loadElements(){
    console.log("hello")
    const userTotal = document.getElementsByClassName("main-totals-usertotal")[0];

    if (userTotal.innerHTML[0] == "+"){
        userTotal.style.color = "green";
    } else{
        userTotal.style.color = "red";
    };

    if (!sessionStorage.getItem("display")){
        sessionStorage.setItem("display", "block")
    } else{
        mainModal.style.display = sessionStorage.getItem("display")
    }

    if (!sessionStorage.getItem("opacity")){
        sessionStorage.setItem("opacity", "1")
    } else{
        mainModal.style.opacity = sessionStorage.getItem("opacity")
    }
}

function blurModal(value){
    if (value === "show"){
        sessionStorage.setItem("opacity", "0");
        mainModal.style.opacity = sessionStorage.getItem("opacity");
        sessionStorage.setItem("display", "none");
        setTimeout(() => {mainModal.style.display = sessionStorage.getItem("display")}, 200);
    } else if (value === "hide"){
        sessionStorage.setItem("display", "block");
        mainModal.style.display = sessionStorage.getItem("display");
        sessionStorage.setItem("opacity", "1");
        setTimeout(() => {mainModal.style.opacity = sessionStorage.getItem("opacity")}, 200);
    }
}


function addNewIncome(){
    var url = '/add_income/';
    incomeAmount = document.getElementsByClassName('income-amount')[0].value
    incomeName = document.getElementsByClassName('income-name')[0].value

    x = document.getElementsByClassName('main-left-list-element-title')

    for (i = 0; i < x.length; i++){
        if (incomeName === document.getElementsByClassName('main-left-list-element-title')[i].innerHTML){
            alert("Name already exists. Please choose another.")
        }
    }

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'income_amount': incomeAmount, 'income_name': incomeName})
    })

    .then((response) =>{
        location.reload()
        return response.json();
    })
}

function deleteIncome(i){
    var url = '/remove_income/';
    incomeName = document.getElementsByClassName('main-left-list-element-title')[i].innerHTML

    if (confirm("Are you sure you want to delete '" + incomeName + "'?")){
        fetch(url, {
            method:'DELETE',
            headers:{
                'Content-Type':'application/json',
                'X-CSRFToken':csrftoken,
            },
            body:JSON.stringify({'income_name': incomeName})
        })
        
        .then((response) =>{
            location.reload()
            return response.json();
        })
    }

}


function addNewExpense(){
    var url = '/add_expense/';
    expenseAmount = document.getElementsByClassName('expense-amount')[0].value
    expenseName = document.getElementsByClassName('expense-name')[0].value
    
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'expense_amount': expenseAmount, 'expense_name': expenseName})
    })
    
    .then((response) =>{
        location.reload()
        return response.json();
    })
}

function deleteExpense(i){
    var url = '/remove_expense/';
    expenseName = document.getElementsByClassName('main-right-list-element-title')[i].innerHTML

    if (confirm("Are you sure you want to delete '" + expenseName + "'?")){
        fetch(url, {
            method:'DELETE',
            headers:{
                'Content-Type':'application/json',
                'X-CSRFToken':csrftoken,
            },
            body:JSON.stringify({'expense_name': expenseName})
        })
        
        .then((response) =>{
            location.reload()
            return response.json();
        })
    }
}

function incomeBtn(i){
    if (i == 0){
        incomeForm.style.display = "flex";
        setTimeout(() => {incomeForm.style.opacity = "1"}, 200);
    };
}


function expenseBtn(i){
    if (i == 0){
        expenseForm.style.display = "flex";
        setTimeout(() => {expenseForm.style.opacity = "1"}, 200);
    };
}
