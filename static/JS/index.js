console.log("INDEX");
import getFetch from "./getFetch.js";
import postFetch from "./postFetch.js";
import truncate from "./truncate.js"


// FETCH
const datas = document.querySelectorAll('[data-id]');
// 

// truncate(datas)


datas.forEach((d) => {

    console.log(d.innerText);
    // truncate(d)
    d.addEventListener("click", () => {
        const value = { inventoryname: d.innerText }
        console.log("you click", value);

        const URL = `${window.origin}/api/inventory/${value.inventoryname}`
        getFetch(URL)
    })


})



// console.log(datas);

// truncate()
















// Get the modal
const myModal = document.getElementById("myModal");
// const myEditModal = document.getElementById("myEditModal");

// const edits = document.querySelectorAll("#editModal");








// Get the button that opens the modal
const myBtn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
const close = document.getElementsByClassName("close")[0];
// const closeEdit = document.getElementsByClassName("closeEdit")[0]

// When the user clicks the button, open the modal 
myBtn.onclick = function () {
    myModal.style.display = "block";

}





// When the user clicks on <span> (x), close the modal
close.onclick = function () {
    myModal.style.display = "none";
    
}



// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == myModal) {
        myModal.style.display = "none";

    }
    
    // else if (event.target == myEditModal) {

    //     myEditModal.style.display = "none";
    // }

    // console.log(event.target);


}





const deletes = document.querySelectorAll(".delete")

deletes.forEach(del =>{

    del.addEventListener("click", ()=>{
        console.log(del.parentElement.parentElement.childNodes[1].firstChild.dataset.id);
        const getInventoryName = del.parentElement.parentElement.childNodes[1].innerText
        // const name_id  = del.parentNode.parentNode.childNodes[1].childNodes[1].dataset.id
        const name_id =  del.parentElement.parentElement.childNodes[1].firstChild.dataset.id
        console.log(name_id);
        const value = {name_id, inventoryName:getInventoryName }
        const URL = `${window.origin}/inventory/update`
        console.log(del.parentElement.parentElement);
        del.parentElement.parentElement.classList.add("animate__animated", "animate__fadeOutLeftBig")
        postFetch(value, URL)     
    })
})







// edits.forEach(edit => {
//     edit.addEventListener("click", () => {
//         const getInventoryName = edit.parentNode.parentNode.childNodes[3].innerText
//         const name_id  = edit.parentNode.parentNode.childNodes[3].childNodes[1].dataset.id

        



//         console.log(getInventoryName);
//         console.log(name_id);
//         myEditModal.style.display = "block";
//         const editInventoryName = document.getElementById("editInventoryName")
//         editInventoryName.value  = getInventoryName
//         console.log(editInventoryName.value );
//         // console.log(close, "Close");



        
//         // const URL = `${window.origin}//inventory/update`
//         // const value = { getInventoryName, editInventoryName,name_id }
//         // console.log(URL);
//         // fetch(URL, {
//         //     method: 'POST',
//         //     credentials: "include",
//         //     cache: 'no-cache',
//         //     body: JSON.stringify(value),
//         //     headers:{
//         //         "content-type":"application/json"
//         //     }
//         // }).then(res => {
//         //     if (res.status !== 200) {
//         //         console.log(`Respond status is not 200 ${res.status}`);
//         //         return;
//         //     }

//         //     res.text().then((data) => {
//         //         console.log(data)
//         //         window.location.replace(URL);
//         //     })
//         // })





//     })

// })
