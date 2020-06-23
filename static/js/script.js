$("input[name='fieldA']").change(e => {
  var n = e.currentTarget.value;
  if (n > 0) {
    console.log("Superieure à Zero")
    $("input[name='fieldD']").hide();
  }else {
    $("input[name='fieldD']").show();
  }
})
