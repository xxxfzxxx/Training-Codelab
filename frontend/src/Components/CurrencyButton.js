import styles from "./CurrencyButton.module.css";

/* 
:currency:
  the current chosen currency
:type:
  string
:changeCurrency:
  function that change currency value on parent
:type:
  function
*/
function CurrencyButton({ currency, changeCurrency }) {
  // ToDo 10.1
  return (
    <>
      <button
        onClick={() => changeCurrency("USD")}
        className={
          currency === "USD"
            ? styles.currencyButtonActive
            : styles.currencyButtonDefault
        }
      >
        USD
      </button>

      <button
        onClick={() => changeCurrency("CNY")}
        className={
          currency === "CNY"
            ? styles.currencyButtonActive
            : styles.currencyButtonDefault
        }
      >
        CNY
      </button>
    </>
  );
}

export default CurrencyButton;
