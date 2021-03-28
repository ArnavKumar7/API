console.log("Whats up")


/**
axios({
	method:'get',
	url: "http://localhost:8000/connect",
}).then(response => {
	var store=response.data
	console.log(response.data)
	var firstdiv= document.getElementById("this is my World")
	firstdiv.innerHTML= store.date
})

axios({
	method:'get'
	url: "https://new-student-db.herokuapp.com/"
}).then(response => {
	var detail=response.data
	console.log(response.data)
	var secdiv= document.getElementById("this is my World")
	secdiv.innerHTML=detail

console.log("End")**/
function studentdb(){
	var name=document.getElementById("name1").value
	var age=document.getElementById("age1").value
	var srn=document.getElementById("SRN1").value
	var comms=document.getElementById("comm1").value
	axios({
		method:'post',
		url: "https://new-student-db.herokuapp.com/details",
		data: {
			student_name: name,
			age: age,
			srn: srn,
			comments: comms
		}
	}).then(response => {
		var store=response.data
		console.log(response.data)
		var firstdiv= document.getElementById("this is my World")
		firstdiv.innerHTML= store
	})
}


