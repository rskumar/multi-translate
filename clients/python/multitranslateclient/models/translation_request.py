# coding: utf-8

"""
    multi-translate

    Multi-Translate is a unified interface on top of various translate APIs providing optimal translations, persistence, fallback.  # noqa: E501

    The version of the OpenAPI document: 0.7.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from multitranslateclient.configuration import Configuration


class TranslationRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'source_text': 'str',
        'to_language': 'str',
        'from_language': 'str',
        'preferred_engine': 'str',
        'with_alignment': 'bool',
        'fallback': 'bool'
    }

    attribute_map = {
        'source_text': 'source_text',
        'to_language': 'to_language',
        'from_language': 'from_language',
        'preferred_engine': 'preferred_engine',
        'with_alignment': 'with_alignment',
        'fallback': 'fallback'
    }

    def __init__(self, source_text=None, to_language=None, from_language=None, preferred_engine='best', with_alignment=False, fallback=False, local_vars_configuration=None):  # noqa: E501
        """TranslationRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._source_text = None
        self._to_language = None
        self._from_language = None
        self._preferred_engine = None
        self._with_alignment = None
        self._fallback = None
        self.discriminator = None

        self.source_text = source_text
        self.to_language = to_language
        if from_language is not None:
            self.from_language = from_language
        if preferred_engine is not None:
            self.preferred_engine = preferred_engine
        if with_alignment is not None:
            self.with_alignment = with_alignment
        if fallback is not None:
            self.fallback = fallback

    @property
    def source_text(self):
        """Gets the source_text of this TranslationRequest.  # noqa: E501

        The text to be translated  # noqa: E501

        :return: The source_text of this TranslationRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_text

    @source_text.setter
    def source_text(self, source_text):
        """Sets the source_text of this TranslationRequest.

        The text to be translated  # noqa: E501

        :param source_text: The source_text of this TranslationRequest.  # noqa: E501
        :type source_text: str
        """
        if self.local_vars_configuration.client_side_validation and source_text is None:  # noqa: E501
            raise ValueError("Invalid value for `source_text`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                source_text is not None and len(source_text) > 200):
            raise ValueError("Invalid value for `source_text`, length must be less than or equal to `200`")  # noqa: E501

        self._source_text = source_text

    @property
    def to_language(self):
        """Gets the to_language of this TranslationRequest.  # noqa: E501

        The ISO-639-1 code of the language to translate the text to  # noqa: E501

        :return: The to_language of this TranslationRequest.  # noqa: E501
        :rtype: str
        """
        return self._to_language

    @to_language.setter
    def to_language(self, to_language):
        """Sets the to_language of this TranslationRequest.

        The ISO-639-1 code of the language to translate the text to  # noqa: E501

        :param to_language: The to_language of this TranslationRequest.  # noqa: E501
        :type to_language: str
        """
        if self.local_vars_configuration.client_side_validation and to_language is None:  # noqa: E501
            raise ValueError("Invalid value for `to_language`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                to_language is not None and len(to_language) > 2):
            raise ValueError("Invalid value for `to_language`, length must be less than or equal to `2`")  # noqa: E501

        self._to_language = to_language

    @property
    def from_language(self):
        """Gets the from_language of this TranslationRequest.  # noqa: E501

        The ISO-639-1 code of the language to translate the text from - if notspecified then detection will be attempted  # noqa: E501

        :return: The from_language of this TranslationRequest.  # noqa: E501
        :rtype: str
        """
        return self._from_language

    @from_language.setter
    def from_language(self, from_language):
        """Sets the from_language of this TranslationRequest.

        The ISO-639-1 code of the language to translate the text from - if notspecified then detection will be attempted  # noqa: E501

        :param from_language: The from_language of this TranslationRequest.  # noqa: E501
        :type from_language: str
        """
        if (self.local_vars_configuration.client_side_validation and
                from_language is not None and len(from_language) > 2):
            raise ValueError("Invalid value for `from_language`, length must be less than or equal to `2`")  # noqa: E501

        self._from_language = from_language

    @property
    def preferred_engine(self):
        """Gets the preferred_engine of this TranslationRequest.  # noqa: E501

        Which translation engine to use. Choices are microsoft, google, amazon, papago, deepl, yandex and best  # noqa: E501

        :return: The preferred_engine of this TranslationRequest.  # noqa: E501
        :rtype: str
        """
        return self._preferred_engine

    @preferred_engine.setter
    def preferred_engine(self, preferred_engine):
        """Sets the preferred_engine of this TranslationRequest.

        Which translation engine to use. Choices are microsoft, google, amazon, papago, deepl, yandex and best  # noqa: E501

        :param preferred_engine: The preferred_engine of this TranslationRequest.  # noqa: E501
        :type preferred_engine: str
        """

        self._preferred_engine = preferred_engine

    @property
    def with_alignment(self):
        """Gets the with_alignment of this TranslationRequest.  # noqa: E501

        Whether to return word alignment information or not  # noqa: E501

        :return: The with_alignment of this TranslationRequest.  # noqa: E501
        :rtype: bool
        """
        return self._with_alignment

    @with_alignment.setter
    def with_alignment(self, with_alignment):
        """Sets the with_alignment of this TranslationRequest.

        Whether to return word alignment information or not  # noqa: E501

        :param with_alignment: The with_alignment of this TranslationRequest.  # noqa: E501
        :type with_alignment: bool
        """

        self._with_alignment = with_alignment

    @property
    def fallback(self):
        """Gets the fallback of this TranslationRequest.  # noqa: E501

        Whether to fallback to the best available engine if the preferred engine does not succeed  # noqa: E501

        :return: The fallback of this TranslationRequest.  # noqa: E501
        :rtype: bool
        """
        return self._fallback

    @fallback.setter
    def fallback(self, fallback):
        """Sets the fallback of this TranslationRequest.

        Whether to fallback to the best available engine if the preferred engine does not succeed  # noqa: E501

        :param fallback: The fallback of this TranslationRequest.  # noqa: E501
        :type fallback: bool
        """

        self._fallback = fallback

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TranslationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TranslationRequest):
            return True

        return self.to_dict() != other.to_dict()
