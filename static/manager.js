$(document).ready(function() {
    $.getJSON('/api/managerlist', function(data) {
        var htm = `<table class="table table-hover">
      <thead>
        <tr>
         <th scope="col">#</th>
         <th scope="col">Name</th>
         <th scope="col">Birth</th>
         <th scope="col">Contact</br>Details</th>
         <th scope="col">Address</th>
         <th scope="col">Picture</th>
         <th scope="col">Update</th>
       </tr>
     </thead>
    <tbody>`
        data.map((item) => {
            htm += `<tr>
  <th scope="row">${item.id}</th>
  <td>${item.firstname} ${item.lastname}</ td>
  <td>${item.gender}<br>${item.dob}</ td>
  <td>${item.emailid}<br>${item.mobileno}</ td>
  <td>${item.address}<br>${item.cityname},${item.statename}</ td>
  <td><img src="/${item.photograph}" width="30"></ td>
  <td><a href='/api/managerbyid?managerid=${item.id}'>Update/Delete</a></td>`


        })
        htm += `</tbody></table>`
        $('#managerData').html(htm)

    })


})