/*

Script Created by Jerome Laliag <jeromelaliag@yahoo.com>

*/

setInterval(function () {
	$("#wanip").load("/cgi-bin/wanip.cgi")
}, 1000);
setInterval(function () {
	$("#openvpnstatus").load("/cgi-bin/openvpnstatus.cgi")
}, 1000);
setInterval(function () {
	$("#vpnstatus").load("/cgi-bin/vpnstatus.cgi")
}, 1000);
setInterval(function () {
	$("#ovpnbutton").load("/cgi-bin/openvpnbutton.cgi")
}, 1000);
setInterval(function () {
	$("#openvpnstartup").load("/cgi-bin/openvpnstartup.cgi")
}, 1000);
setInterval(function () {
	$("#logs").load("/cgi-bin/logs.cgi")
}, 1000);
setInterval(function () {
	$("#usedata").load("/cgi-bin/usedata.cgi")
}, 1000);
setInterval(function () {
	$("#vpnip").load("/cgi-bin/vpnip.cgi")
}, 1000);
$(document).ready(function () {
	var t = $("#username").val();
	$.ajax({
		type: "GET",
		url: "/cgi-bin/user.cgi",
		success: function (t) {
			$("#user").val(t)
		}
	})
});
$(document).ready(function () {
	var t = $("#password").val();
	$.ajax({
		type: "GET",
		url: "/cgi-bin/pass.cgi",
		success: function (t) {
			$("#pass").val(t)
		}
	})
});
$(document).ready(function () {
	var t = $("#password").val();
	$.ajax({
		type: "GET",
		url: "/cgi-bin/password.cgi",
		success: function (t) {
			$("#password").val(t)
		}
	})
});

function connect() {
	$.get("/cgi-bin/connect.cgi", function (t) {
		"" != t && alert(t)
	})
};

function disconnect() {
	$.get("/cgi-bin/disconnect.cgi", function (t) {
		"" != t && alert(t)
	})
};

function addopenvpnstartup() {
	$.get("/cgi-bin/addopenvpnstartup.cgi", function (t) {
		"" != t && alert(t)
	})
};

function removeopenvpnstartup() {
	$.get("/cgi-bin/removeopenvpnstartup.cgi", function (t) {
		"" != t && alert(t)
	})
};

function wanipchanger() {
	$.get("/cgi-bin/changewanip.cgi", function (t) {
		alert("Success.")
	})
};

function clearlogs() {
	$.get("/cgi-bin/clearlogs.cgi")
};
window.setInterval(function () {
	var t = document.getElementById("logs");
	t.scrollTop = t.scrollHeight
});

function copylogs() {
	document.getElementById("logs").select(), document.execCommand("copy"), alert("Success.")
};

$(document).ready(function () {
	$('input').keydown(function (event) {
		if (event.keyCode == 13) {
			event.preventDefault();
			return false;
		}
	});
});