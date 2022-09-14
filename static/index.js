$(".mode-toggle").on("click", () => {
  if ($("body").hasClass("dark-mode")) {
    $("body").removeClass("dark-mode");
    $(".mode-toggle").text("Dark Mode");
  } else {
    $("body").addClass("dark-mode");
    $(".mode-toggle").text("Go Blind");
  }
});
