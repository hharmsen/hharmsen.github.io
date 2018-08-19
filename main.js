/**
 * Main logic of this utility.
 * 
 */

function drawMenu(key) {
	var list = document.getElementById("menu");
	listItems = list.children;
	for (var i = listItems.length; i >= 0; i -= 1) {
		if (listItems[i] != undefined) {
			list.removeChild(listItems[i]);
		}
	}
	for (var i = 0; i < menu[key].length; i += 1) {
		listItem = document.createElement("li");
		anchor = document.createElement("a");
		if (menu[key][i].url && (menu[key][i].url.indexOf("/") > -1)) {
			anchor.setAttribute("href", menu[key][i].url);
		} else {
			anchor.setAttribute("onclick", "drawMenu(\"" + menu[key][i].url
					+ "\");");
		}
		anchor.innerHTML = menu[key][i].label;
		listItem.appendChild(anchor);
		list.appendChild(listItem);
	}
	sessionStorage.setItem("favourites", key);

	return false;
}

var key = sessionStorage.getItem("favourites");
if (!key) {
    key = "main";
}
drawMenu(key);
