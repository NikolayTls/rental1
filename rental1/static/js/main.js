function showModal(data)
{
   //you can do anything with data, or pass more data to this function. i set this data to modal header for example
   $("#myModal .modal-title").html(data)
   $("#myModal").modal();
}


