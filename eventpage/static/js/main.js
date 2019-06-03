var d = document.referrer
if( d == 'http://127.0.0.1:8000/index/' ||
    d == 'http://127.0.0.1:8000/lavinia-event-arajji/' ||
    d == 'http://127.0.0.1:8000/lavinia-event-normal/' ||
    d == 'http://127.0.0.1:8000/rainbowhouse-event-arajji/' ||
    d == 'http://127.0.0.1:8000/rainbowhouse-event-normal/' ||
    d == 'http://www.spooncomics.com/viewer/1593/22287' ||
    d == 'http://www.spooncomics.com/viewer/1593/22288' ||
    d == 'http://www.spooncomics.com/viewer/1558/22174' ||
    d == 'http://www.spooncomics.com/viewer/1558/22295'){
    alert(d);
}else{
    alert('잘못된 접근입니다');
    window.location.href = 'http://www.spooncomics.com';
}