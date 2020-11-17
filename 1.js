const fetch = require('node-fetch');

let body = "{\"productInfoMapping\":{\"isWhiteGloveRequired\":false,\"weightUnitString\":\"pounds\",\"subCategory\":\"20106048\",\"fnsku\":\"\",\"dimensionUnit\":\"inches\",\"link\":\"http://www.amazon.com/gp/product/B07W95N8F7/ref=silver_xx_cont_revecalc\",\"binding\":\"\",\"title\":\"Degrees Of Comfort [Advanced] Microplush Electric Blanket with Auto Shut Off | Heating Blankets for Bed & Living Room | Machine Washable | UL Certified and EMF Radiation Safe - Twin, Blue\",\"dimensionUnitString\":\"inches\",\"price\":0,\"imageUrl\":\"https://m.media-amazon.com/images/I/51cSwb-BOyL._SCLZZZZZZZ__SL120_.jpg\",\"height\":"+process.argv[2].trim()+",\"isAfn\":false,\"gl\":\"gl_home\",\"length\":"+process.argv[3]+",\"isAsinLimits\":true,\"weight\":"+process.argv[4]+",\"originalUrl\":\"\",\"productGroup\":\"\",\"width\":"+process.argv[5]+",\"thumbStringUrl\":\"https://m.media-amazon.com/images/I/51cSwb-BOyL._SCLZZZZZZZ__SL80_.jpg\",\"asin\":\""+process.argv[6]+"\",\"encryptedMarketplaceId\":\"\",\"weightUnit\":\"pounds\"},\"afnPriceStr\":0,\"mfnPriceStr\":5,\"mfnShippingPriceStr\":0,\"currency\":\"USD\",\"marketPlaceId\":\"ATVPDKIKX0DER\",\"hasFutureFee\":false,\"futureFeeDate\":\"2020-03-19 08:00:00\",\"hasTaxPage\":true}";

fetch("https://sellercentral.amazon.com/fba/profitabilitycalculator/getafnfee?profitcalcToken=goTQ8tOV7SdgWVzfaR4ZyqbsRZEmgu9CA2lBWygAAAAMAAAAAF%2BZC1hyYXcAAAAAFVfwLBerPie4v1Ep////", {
  "headers": {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "en-US,en;q=0.9,es;q=0.8",
    "content-type": "application/json;charset=UTF-8",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest"
  },
  "referrer": "https://sellercentral.amazon.com/hz/fba/profitabilitycalculator/index?lang=en_US",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": body,
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
}) .then(res => res.text())
    .then(body => console.log(body));

    console.log(process.argv[2])