const collapseElems = document.querySelectorAll(".collapsable");

for (let item of collapseElems) {
    item.addEventListener(
        "click",
        () => {
            item.classList.toggle("active");

            let content = item.nextElementSibling;

            if (content.style.maxHeight) {
                content.style.maxHeight = null;
                content.style.overflow = "hidden";
            } else {
                content.style.maxHeight = content.scrollHeight + "px";
                content.style.overflow = "auto";
            }
        });
}
