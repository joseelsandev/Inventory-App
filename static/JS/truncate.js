const truncate = (strs,max = 10) =>{

    strs.forEach(str =>{
        // console.log(str.innerText)
        // console.log(str.innerText.length)
        // const  max = 10
        
        // condition ? expressionIfTrue : expressionIfFalse
        return str.innerText =  str.innerText.length > max  ?  str.innerText.slice(0,max) + " . . ." : str.innerText
    
    })
    

}


export default truncate;