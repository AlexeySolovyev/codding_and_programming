var month_of_names = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"];
var text_olymp = {org_1_1: "Кафедра физико-математического образования Санкт-Петербургской",org_1_2: "академии постдипломного педагогического образования",org_2_1: "МетаШкола. Информационные технологии",attr_1: "Открытая российская математическая",attr_2: "интернет-олимпиада для школьников",title_for_teachers: "«Осень 2015»",sertificate: "СЕРТИФИКАТ",sertificate_sert: "удостоверяет, что",sertificate_part: "участвовал(а) в интернет-олимпиаде",sertificate_number: "Сертификат №",diploma: "ДИПЛОМ",diploma_degree: "степени",diploma_award: "награждается",diploma_number: "Диплом №",thanks: "БЛАГОДАРНОСТЬ",thanks_award: "награждается",thanks_for: "за отличную подготовку учащихся",thanks_to: "учитель",thanks_number: "№ ",committee: "Оргкомитет",member: [{position: "Заведующий кафедрой",name: "Е. Ю. Лукичева",phd: "к. п. н."}, {position: "Учитель ФМЛ № 366",name: "И. И. Трушова",phd: ""}, {position: "Руководитель проекта",name: "Е. В. Смыкалова",phd: "к. п. н."}],city: "Санкт-Петербург"};
function getLocaleDate(day, month, year, langId) {
    var s = "" + day;
    if (2 == langId) {
        s += "."
    }
    return s + " " + month_of_names[month] + " " + year
}
function getLocaleDegree(degreeId, langId) {
    if (1 > degreeId || degreeId > 3) {
        return "error in degreeId"
    }
    if (2 == langId) {
        return "" + degreeId + "."
    }
    if (1 == degreeId) {
        return "I"
    } else if (2 == degreeId) {
        return "II"
    } else {
        return "III"
    }
}
function drawAward(textCommon, textOlymp, img_url, imageWidth, olympId, gopts) {
    "use strict";
    var opts = gopts || {};
    var top_line = 80;
    var middle_line = 266;
    var bottom_line = 726;
    var sert_line = 1010;
    var offsetLeft = 110;
    var canvas = document.getElementById("canvasDiploma");
    var context = canvas.getContext("2d");
    var img = new Image;
    var x0 = Math.round(imageWidth / 2);
    img.onload = function() {
        var fontSizeXXL = 14;
        var fontSizeXL = 18;
        var fontSizeL = 22;
        var fontSizeLV = 30;
        var fontSizeLX = 48;
        var gapXL = 40;
        var gapL = 60;
        var gapLX = 80;
        context.drawImage(img, 0, 0);
        context.textAlign = "center";
        context.fillStyle = "#220";
        context.shadowColor = "#ccc";
        context.shadowOffsetX = 5;
        context.shadowOffsetY = 5;
        context.shadowBlur = 5;
        y = top(top_line);
        if (12 == textCommon.klassNumber) {
            y = teacher_middle_thanks(middle_line)
        } else {
            if (0 == textCommon.degreeId) {
                y = pupil_middle_sertificate(middle_line)
            } else {
                y = pupil_middle_diploma(middle_line)
            }
        }
        var y = bottom(bottom_line);
        function top(y) {
            context.font = getFont(fontSizeXXL);
            context.fillText(textOlymp.org_1_1, x0, y);
            y += 1.5 * fontSizeXXL;
            context.fillText(textOlymp.org_1_2, x0, y);
            y += 2 * fontSizeXXL;
            context.fillText(textOlymp.org_2_1, x0, y);
            y += gapL;
            context.font = getFont(fontSizeL);
            context.fillText(textOlymp.attr_1, x0, y);
            y += 1.5 * fontSizeL;
            context.fillText(textOlymp.attr_2, x0, y);
            return y
        }
        function pupil_middle_sertificate(y) {
            context.fillText(textCommon.title, x0, y);
            y += gapLX;
            if (2 == textCommon.langId) {
                context.font = getFont(fontSizeLV)
            } else {
                context.font = getFont(fontSizeLX)
            }
            context.fillText(textOlymp.sertificate, x0, y);
            y = y + gapL;
            context.font = getFont(fontSizeL);
            context.fillText(textOlymp.sertificate_sert, x0, y);
            y = y + gapL;
            y = fio(y);
            y = y + gapL;
            context.font = getFont(fontSizeL);
            context.fillText(textOlymp.sertificate_part, x0, y);
            return y
        }
        function pupil_middle_diploma(y) {
            context.fillText(textCommon.title, x0, y);
            y += gapXL + gapL;
            context.font = getFont(fontSizeLX);
            context.fillText(textOlymp.diploma, x0, y);
            y = y + gapL;
            context.font = getFont(fontSizeL);
            context.fillText(textCommon.degree + " " + textOlymp.diploma_degree, x0, y);
            if ("" != textOlymp.diploma_award) {
                y = y + gapL;
                context.font = getFont(fontSizeL);
                context.fillText(textOlymp.diploma_award, x0, y);
                y = y + gapL;
                y = fio(y)
            } else {
                y = y + gapL;
                y = fio(y);
                y = y + gapL
            }
            return y
        }
        function teacher_middle_thanks(y) {
            context.fillText(textOlymp.title_for_teachers, x0, y);
            y += gapXL + gapL;
            context.font = getFont(fontSizeLX);
            context.fillText(textOlymp.thanks, x0, y);
            context.font = getFont(fontSizeL);
            y = y + gapL;
            context.fillText(textOlymp.thanks_award, x0, y);
            y = y + gapL;
            context.fillText(textOlymp.thanks_to, x0, y);
            y = y + gapXL;
            y = fio(y);
            y = y + gapL;
            context.fillText(textOlymp.thanks_for, x0, y);
            return y
        }
        function bottom(y) {
            var offsetLeftName = 475;
            context.font = getFont(fontSizeL);
            context.fillText(textOlymp.committee, x0, y);
            context.font = getFont(fontSizeXL);
            context.textAlign = "left";
            y += gapXL;
            context.fillText(textOlymp.member[0].position, offsetLeft, y);
            context.fillText(textOlymp.member[0].name, offsetLeftName, y);
            y += 1.5 * fontSizeXL;
            context.fillText(textOlymp.member[0].phd, offsetLeft, y);
            y += gapXL;
            context.fillText(textOlymp.member[1].position, offsetLeft, y);
            context.fillText(textOlymp.member[1].name, offsetLeftName, y);
            y += gapXL;
            context.fillText(textOlymp.member[2].position, offsetLeft, y);
            context.fillText(textOlymp.member[2].name, offsetLeftName, y);
            y += 1.5 * fontSizeXL;
            context.fillText(textOlymp.member[2].phd, offsetLeft, y);
            y += gapXL;
            context.textAlign = "center";
            context.font = getFont(fontSizeXL);
            context.fillText(textOlymp.city, x0, y);
            y += 2 * fontSizeXL;
            if (12 == textCommon.klassNumber) {
                context.fillText(textCommon.dateRange, x0, y)
            } else {
                context.fillText(textCommon.date, x0, y)
            }
            context.font = getFont(fontSizeXXL);
            context.textAlign = "center";
            if (12 == textCommon.klassNumber) {
                context.fillText(textOlymp.thanks_number + " " + textCommon.thanksNumber, imageWidth / 2, sert_line)
            } else if (0 == textCommon.degreeId) {
                context.fillText(textOlymp.sertificate_number + " " + textCommon.sertNumber, imageWidth / 2, sert_line)
            } else {
                context.fillText(textOlymp.diploma_number + " " + textCommon.sertNumber, imageWidth / 2, sert_line)
            }
            return y
        }
        function fio(y) {
            context.font = getFont(fontSizeL);
            context.fillText(textCommon.name, x0, y);
            if (12 > textCommon.klassNumber) {
                y = y + gapXL;
                context.fillText(textCommon.klass, x0, y)
            }
            y = y + gapXL;
            context.fillText(textCommon.school, x0, y);
            y = y + gapXL;
            context.fillText(textCommon.address, x0, y);
            return y
        }
        function getFont(fontSize) {
            return "400 " + fontSize + "pt Arial"
        }
    };
    img.src = img_url
}
