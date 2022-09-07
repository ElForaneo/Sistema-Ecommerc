const phoneInputField = document.querySelector("#phone");
const phoneInput = window.intlTelInput(phoneInputField, {
  utilsScript:
	"https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
	separateDialCode: true,
	preferredCountries: ["mx", "us"],
	initialCountry:"mx",
	onlyCountries: ["mx", "us","cu", "ve", "ar", "es","ca","ec","pe",""],
});

function formatPhoneNumber(value) {
	if (!value) return value;
	const phoneNumber = value.replace(/[^\d]/g, '');
	const phoneNumberLength = phoneNumber.length;
	if (phoneNumberLength < 4) return phoneNumber;
	if (phoneNumberLength < 7) {
	  return `(${phoneNumber.slice(0, 3)}) ${phoneNumber.slice(3)}`;
	}
	return `(${phoneNumber.slice(0, 3)}) ${phoneNumber.slice(
	  3,
	  6
	)} ${phoneNumber.slice(6, 9)}`;
  }

  function phoneNumberFormatter() {
	const inputField = document.getElementById('phone');
	const formattedInputValue = formatPhoneNumber(inputField.value);
	inputField.value = formattedInputValue;
  }