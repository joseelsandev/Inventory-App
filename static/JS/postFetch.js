const postFetch = (value, URL) => {
    fetch(URL, {
        method: 'POST',
        credentials: "include",
        cache: 'no-cache',
        body: JSON.stringify(value),
        headers: {
            "content-type": "application/json"
        }
    }).then(res => {
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

export default postFetch;