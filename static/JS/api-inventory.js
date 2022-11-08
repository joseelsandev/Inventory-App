import truncate from "./truncate.js"
import getFetch from "./getFetch.js"
import deleteFetch from "./deleteFetch.js"

console.log(window.origin)

// const add = document.querySelector(".add")
// const sku = document.getElementById("sku")

const edits = document.querySelectorAll(".edit")
const h1 = document.querySelector("h1")
const inventoryName = h1.dataset.id

const deletes = document.querySelectorAll(".delete")



edits.forEach(edit => {
    edit.addEventListener("click", () => {

        const inventoryId = edit.parentElement.parentElement.id;
        const URL = `${window.origin}/api/inventory/${inventoryName}/${inventoryId}`
        const value = { inventoryName, inventoryId }
        console.log(URL);
        getFetch(URL)
    })
});


const skus = document.querySelectorAll(".sku")
const titles = document.querySelectorAll(".title")
const locations = document.querySelectorAll(".location")
const control = document.querySelectorAll(".form-control")

console.log(control);



// truncate values
truncate(skus)
truncate(titles)
truncate(locations)


// const truncate = (strs) =>{

// console.log(strs);



// }

// truncate(skus)

// skus[1].innerText = "AA"



// animate__backOutLeft
deletes.forEach(del => {
    del.addEventListener("click", () => {
        const inventoryId = del.parentElement.parentElement.id;
        const URL = `${window.origin}/api/inventory/${inventoryName}`
        const value = { inventoryName, inventoryId }
        console.log(URL);

        del.parentElement.parentElement.classList.add("animate__animated", "animate__backOutLeft")
       
    //    console.log(del.parentElement.parentElement);
        deleteFetch(value, URL);

    })


});


// add.addEventListener("click",()=>{
//     // console.log("ADD")
//     // window.location.replace(URL);
//     console.log(sku.value);
//     const value = { sku: sku.value}

//     const URL = `${window.origin}/api/inventory/${inventoryName}`
//     console.log(URL);
//     fetch(URL, {
//         method: "POST",
//         credentials: "include",
//         body: JSON.stringify(value),
//         cache:"no-cache",
//         headers: new Headers({ 
//             "content-type":"application/json"
//         })
//     })
//     .then((res)=>{
//         if (res.status !== 200 ){
//             console.log(`Respond status is not 200 ${res.status}`);
//             return;
//         }
//         res.text().then((data)=>{
//             console.log(data)
//             window.location.replace(URL);
//         })
//     })
// })


window.addEventListener("DOMContentLoaded", () => {
    const quantity = document.getElementById('quantity')
    quantity.value = ""
    console.log(quantity.value);
})
