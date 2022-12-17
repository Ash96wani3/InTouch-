var popupModel = document.querySelector(".model-container");
var popupModelClose = document.querySelector(".model-close");

window.addEventListener('load', ()=>{
    setTimeout(()=>{        
        popupModel.style.transform ="translateX(0)";
    }, 3000);
});

popupModelClose.addEventListener('click', ()=>{
    popupModel.style.transform = "translateX(110%)";
});
