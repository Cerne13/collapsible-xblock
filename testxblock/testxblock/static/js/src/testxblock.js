const collapseElems = document.querySelectorAll(".collapsable");

for (let item of collapseElems) {
    console.log(item)
    item.addEventListener(
        "click",
        () => {
            item.classList.toggle("active");

            let content = item.nextElementSibling;

            // if (content.style.display === "block") {
            //     content.style.display = "none";
            // } else {
            //     content.style.display = "block";
            // }

            if (content.style.maxHeight) {
                content.style.maxHeight = null;
            } else {
                content.style.maxHeight = content.scrollHeight + "px";
            }
        });
}
