const getFetch = (URL) =>{

    fetch(URL, {
        method: "GET",
        credentials: "include",
        cache: "no-cache",
        redirect: 'follow',
        headers: new Headers({
            "content-type": "application/json"
        })
    })
        .then((res) => {
            if (res.status !== 200) {
                console.log(`Respond status is not 200 ${res.status}`);
                return;
            }
            res.text().then((data) => {
                console.log(data)
                window.location.replace(URL);
            })
        })



}




export default getFetch;