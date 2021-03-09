function validate(username) {
  // Write the code that goes here
  if (username) {
    return reqLength(username) && countHyphen(username) && startWithLetter(username)
      && !endsWithHyphen(username) && validateChars(username)
  }

  return false;
}

function validateChars(username) {
  let arrUserName = username.split("")

  for (i = 0; i < arrUserName.length; i++) {
    if (isLetterOrNumber(arrUserName[i]) || arrUserName[i] === '-') {
      continue;
    } else {
      return false;
    }
  }

  return true;
}

function reqLength(username) {
  return username.length > 5 || username.length < 17;
}


function countHyphen(username) {
  let counter = 0;
  let arrUserName = username.split("")

  arrUserName.forEach(s => {
    if (s === "-") {
      counter++
    }
  })

  return counter === 1 || counter === 0;
}


function startWithLetter(username) {
  return isLetter(username[0]);
}

function isLetter(str) {
  return str.length === 1 && str.match(/[a-z]/i);
}

function isLetterOrNumber(str) {
  return str.length === 1 && str.match(/^[0-9a-zA-Z]+$/);
}

function endsWithHyphen(username) {
  return username[username.length - 1] === '-';
}

console.log(validate('Mike-Standish')); // Valid username
console.log(validate('Mike Standish')); // Invalid username

console.log(reqLength('Mike Standis             h'))