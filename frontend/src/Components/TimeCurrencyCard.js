import styles from "./TimeCurrencyCard.module.css";

/* 
:currency:
    the current chose currency
:type:
    string
:showData:
    array of bitcoin data object with timestamp and price
:type:
    list[{dict}]
*/
function TimeCurrencyCard({ currency, showData }) {
  // ToDo 10.2.1
  /* 
    set price text color
    :index:
        the index of the current object
    :type:
        int
    :return:
        CSS classname
    :rtype:
        CSS  Object
    */

  const priceColor = (index) => {
    if (index === 0) {
      return styles.priceContainerEqual;
    }
    const curr = showData[index]["price"];
    const prev = showData[index - 1]["price"];
    if (curr === prev) {
      return styles.priceContainerEqual;
    } else if (curr > prev) {
      return styles.priceContainerUp;
    } else {
      return styles.priceContainerDown;
    }
  };

  // ToDo 10.2.2
  /* 
    set arrow sign for price
    :index:
        the index of the current object
    :type:
        int
    :return:
        an arrow "↑" "↓" or '-' to show the price change status
    :rtype:
        string
    */
  const arrowSign = (index) => {
    if (index === 0) {
      return "-";
    }
    const curr = showData[index]["price"];
    const prev = showData[index - 1]["price"];
    if (curr === prev) {
      return "-";
    } else if (curr > prev) {
      return "↑";
    } else {
      return "↓";
    }
  };

  // ToDo 10.2.3
  return (
    <>
      {/* reference for .map https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map */}
      {showData.map((d, index) => (
        <>
          {/* use {currency === 'USD' ? "$" : *other currency sign*} to set the currency notation  
                reference https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator */}
          <div>{d["timestamp"]}</div>
          <div className={priceColor(index)}>
            {currency === "USD" ? "$" : "￥"}
            {d["price"]}
            {arrowSign(index)}
          </div>
        </>
      ))}
    </>
  );
}

export default TimeCurrencyCard;
