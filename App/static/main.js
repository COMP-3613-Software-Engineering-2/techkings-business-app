
async function getUserData(){
    const response = await fetch('/api/users');
    return response.json();
}

function loadTable(users){
    const table = document.querySelector('#result');
    for(let user of users){
        table.innerHTML += `<tr>
            <td>${user.id}</td>
            <td>${user.username}</td>
        </tr>`;
    }
}

//To deal with finding groups
async function getGroupData(){
    const response = await fetch('/api/groups');
    return response.json();
}

function loadTable(groups){
    const table = document.querySelector('#result');
    for(let group of groups){
        table.innerHTML += `<tr>
            <td>${group.id}</td>
            <td>${group.groupname}</td>
        </tr>`;
    }
}


async function main(){
    const users = await getUserData();
    loadTable(users);
}

async function main(){
    const groups = await getGroupData();
    loadTable(groups);
}


main();