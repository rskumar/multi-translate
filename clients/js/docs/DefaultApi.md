# @RekonOssMultiTranslate.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSupportedEnginesAvailableEnginesGet**](DefaultApi.md#getSupportedEnginesAvailableEnginesGet) | **GET** /available-engines | Get Supported Engines
[**getSupportedLanguagesSupportedLanguagesGet**](DefaultApi.md#getSupportedLanguagesSupportedLanguagesGet) | **GET** /supported-languages | Get Supported Languages
[**readyGet**](DefaultApi.md#readyGet) | **GET** / | Ready
[**translatePostTranslatePost**](DefaultApi.md#translatePostTranslatePost) | **POST** /translate | Translate Post
[**translateTranslateGet**](DefaultApi.md#translateTranslateGet) | **GET** /translate | Translate



## getSupportedEnginesAvailableEnginesGet

> [String] getSupportedEnginesAvailableEnginesGet()

Get Supported Engines

### Example

```javascript
import @RekonOssMultiTranslate from '@rekon-oss/multi-translate';

let apiInstance = new @RekonOssMultiTranslate.DefaultApi();
apiInstance.getSupportedEnginesAvailableEnginesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSupportedLanguagesSupportedLanguagesGet

> {String: [String]} getSupportedLanguagesSupportedLanguagesGet()

Get Supported Languages

### Example

```javascript
import @RekonOssMultiTranslate from '@rekon-oss/multi-translate';

let apiInstance = new @RekonOssMultiTranslate.DefaultApi();
apiInstance.getSupportedLanguagesSupportedLanguagesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**{String: [String]}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readyGet

> String readyGet()

Ready

### Example

```javascript
import @RekonOssMultiTranslate from '@rekon-oss/multi-translate';

let apiInstance = new @RekonOssMultiTranslate.DefaultApi();
apiInstance.readyGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## translatePostTranslatePost

> TranslationResponse translatePostTranslatePost(translationRequest)

Translate Post

### Example

```javascript
import @RekonOssMultiTranslate from '@rekon-oss/multi-translate';

let apiInstance = new @RekonOssMultiTranslate.DefaultApi();
let translationRequest = new @RekonOssMultiTranslate.TranslationRequest(); // TranslationRequest | 
apiInstance.translatePostTranslatePost(translationRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **translationRequest** | [**TranslationRequest**](TranslationRequest.md)|  | 

### Return type

[**TranslationResponse**](TranslationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## translateTranslateGet

> TranslationResponse translateTranslateGet(sourceText, toLanguage, opts)

Translate

### Example

```javascript
import @RekonOssMultiTranslate from '@rekon-oss/multi-translate';

let apiInstance = new @RekonOssMultiTranslate.DefaultApi();
let sourceText = "sourceText_example"; // String | The text to be translated
let toLanguage = "toLanguage_example"; // String | The ISO-639-1 code of the language to translate the text to
let opts = {
  'fromLanguage': "fromLanguage_example", // String | The ISO-639-1 code of the language to translate the text from - if notspecified then detection will be attempted
  'preferredEngine': "'best'", // String | Which translation engine to use. Choices are microsoft, google, amazon, papago, deepl, yandex and best
  'withAlignment': false, // Boolean | Whether to return word alignment information or not
  'fallback': false // Boolean | Whether to fallback to the best available engine if the preferred engine does not succeed
};
apiInstance.translateTranslateGet(sourceText, toLanguage, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sourceText** | **String**| The text to be translated | 
 **toLanguage** | **String**| The ISO-639-1 code of the language to translate the text to | 
 **fromLanguage** | **String**| The ISO-639-1 code of the language to translate the text from - if notspecified then detection will be attempted | [optional] 
 **preferredEngine** | **String**| Which translation engine to use. Choices are microsoft, google, amazon, papago, deepl, yandex and best | [optional] [default to &#39;best&#39;]
 **withAlignment** | **Boolean**| Whether to return word alignment information or not | [optional] [default to false]
 **fallback** | **Boolean**| Whether to fallback to the best available engine if the preferred engine does not succeed | [optional] [default to false]

### Return type

[**TranslationResponse**](TranslationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

