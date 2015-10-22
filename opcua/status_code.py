#AUTOGENERATED!!!


class StatusCodes:
    Good = 0
    Uncertain = 0x40000000
    Bad = 0x80000000
    BadUnexpectedError = 0x80010000
    BadInternalError = 0x80020000
    BadOutOfMemory = 0x80030000
    BadResourceUnavailable = 0x80040000
    BadCommunicationError = 0x80050000
    BadEncodingError = 0x80060000
    BadDecodingError = 0x80070000
    BadEncodingLimitsExceeded = 0x80080000
    BadRequestTooLarge = 0x80B80000
    BadResponseTooLarge = 0x80B90000
    BadUnknownResponse = 0x80090000
    BadTimeout = 0x800A0000
    BadServiceUnsupported = 0x800B0000
    BadShutdown = 0x800C0000
    BadServerNotConnected = 0x800D0000
    BadServerHalted = 0x800E0000
    BadNothingToDo = 0x800F0000
    BadTooManyOperations = 0x80100000
    BadTooManyMonitoredItems = 0x80DB0000
    BadDataTypeIdUnknown = 0x80110000
    BadCertificateInvalid = 0x80120000
    BadSecurityChecksFailed = 0x80130000
    BadCertificateTimeInvalid = 0x80140000
    BadCertificateIssuerTimeInvalid = 0x80150000
    BadCertificateHostNameInvalid = 0x80160000
    BadCertificateUriInvalid = 0x80170000
    BadCertificateUseNotAllowed = 0x80180000
    BadCertificateIssuerUseNotAllowed = 0x80190000
    BadCertificateUntrusted = 0x801A0000
    BadCertificateRevocationUnknown = 0x801B0000
    BadCertificateIssuerRevocationUnknown = 0x801C0000
    BadCertificateRevoked = 0x801D0000
    BadCertificateIssuerRevoked = 0x801E0000
    BadUserAccessDenied = 0x801F0000
    BadIdentityTokenInvalid = 0x80200000
    BadIdentityTokenRejected = 0x80210000
    BadSecureChannelIdInvalid = 0x80220000
    BadInvalidTimestamp = 0x80230000
    BadNonceInvalid = 0x80240000
    BadSessionIdInvalid = 0x80250000
    BadSessionClosed = 0x80260000
    BadSessionNotActivated = 0x80270000
    BadSubscriptionIdInvalid = 0x80280000
    BadRequestHeaderInvalid = 0x802A0000
    BadTimestampsToReturnInvalid = 0x802B0000
    BadRequestCancelledByClient = 0x802C0000
    GoodSubscriptionTransferred = 0x002D0000
    GoodCompletesAsynchronously = 0x002E0000
    GoodOverload = 0x002F0000
    GoodClamped = 0x00300000
    BadNoCommunication = 0x80310000
    BadWaitingForInitialData = 0x80320000
    BadNodeIdInvalid = 0x80330000
    BadNodeIdUnknown = 0x80340000
    BadAttributeIdInvalid = 0x80350000
    BadIndexRangeInvalid = 0x80360000
    BadIndexRangeNoData = 0x80370000
    BadDataEncodingInvalid = 0x80380000
    BadDataEncodingUnsupported = 0x80390000
    BadNotReadable = 0x803A0000
    BadNotWritable = 0x803B0000
    BadOutOfRange = 0x803C0000
    BadNotSupported = 0x803D0000
    BadNotFound = 0x803E0000
    BadObjectDeleted = 0x803F0000
    BadNotImplemented = 0x80400000
    BadMonitoringModeInvalid = 0x80410000
    BadMonitoredItemIdInvalid = 0x80420000
    BadMonitoredItemFilterInvalid = 0x80430000
    BadMonitoredItemFilterUnsupported = 0x80440000
    BadFilterNotAllowed = 0x80450000
    BadStructureMissing = 0x80460000
    BadEventFilterInvalid = 0x80470000
    BadContentFilterInvalid = 0x80480000
    BadFilterOperatorInvalid = 0x80C10000
    BadFilterOperatorUnsupported = 0x80C20000
    BadFilterOperandCountMismatch = 0x80C30000
    BadFilterOperandInvalid = 0x80490000
    BadFilterElementInvalid = 0x80C40000
    BadFilterLiteralInvalid = 0x80C50000
    BadContinuationPointInvalid = 0x804A0000
    BadNoContinuationPoints = 0x804B0000
    BadReferenceTypeIdInvalid = 0x804C0000
    BadBrowseDirectionInvalid = 0x804D0000
    BadNodeNotInView = 0x804E0000
    BadServerUriInvalid = 0x804F0000
    BadServerNameMissing = 0x80500000
    BadDiscoveryUrlMissing = 0x80510000
    BadSempahoreFileMissing = 0x80520000
    BadRequestTypeInvalid = 0x80530000
    BadSecurityModeRejected = 0x80540000
    BadSecurityPolicyRejected = 0x80550000
    BadTooManySessions = 0x80560000
    BadUserSignatureInvalid = 0x80570000
    BadApplicationSignatureInvalid = 0x80580000
    BadNoValidCertificates = 0x80590000
    BadIdentityChangeNotSupported = 0x80C60000
    BadRequestCancelledByRequest = 0x805A0000
    BadParentNodeIdInvalid = 0x805B0000
    BadReferenceNotAllowed = 0x805C0000
    BadNodeIdRejected = 0x805D0000
    BadNodeIdExists = 0x805E0000
    BadNodeClassInvalid = 0x805F0000
    BadBrowseNameInvalid = 0x80600000
    BadBrowseNameDuplicated = 0x80610000
    BadNodeAttributesInvalid = 0x80620000
    BadTypeDefinitionInvalid = 0x80630000
    BadSourceNodeIdInvalid = 0x80640000
    BadTargetNodeIdInvalid = 0x80650000
    BadDuplicateReferenceNotAllowed = 0x80660000
    BadInvalidSelfReference = 0x80670000
    BadReferenceLocalOnly = 0x80680000
    BadNoDeleteRights = 0x80690000
    UncertainReferenceNotDeleted = 0x40BC0000
    BadServerIndexInvalid = 0x806A0000
    BadViewIdUnknown = 0x806B0000
    BadViewTimestampInvalid = 0x80C90000
    BadViewParameterMismatch = 0x80CA0000
    BadViewVersionInvalid = 0x80CB0000
    UncertainNotAllNodesAvailable = 0x40C00000
    GoodResultsMayBeIncomplete = 0x00BA0000
    BadNotTypeDefinition = 0x80C80000
    UncertainReferenceOutOfServer = 0x406C0000
    BadTooManyMatches = 0x806D0000
    BadQueryTooComplex = 0x806E0000
    BadNoMatch = 0x806F0000
    BadMaxAgeInvalid = 0x80700000
    BadHistoryOperationInvalid = 0x80710000
    BadHistoryOperationUnsupported = 0x80720000
    BadInvalidTimestampArgument = 0x80BD0000
    BadWriteNotSupported = 0x80730000
    BadTypeMismatch = 0x80740000
    BadMethodInvalid = 0x80750000
    BadArgumentsMissing = 0x80760000
    BadTooManySubscriptions = 0x80770000
    BadTooManyPublishRequests = 0x80780000
    BadNoSubscription = 0x80790000
    BadSequenceNumberUnknown = 0x807A0000
    BadMessageNotAvailable = 0x807B0000
    BadInsufficientClientProfile = 0x807C0000
    BadStateNotActive = 0x80BF0000
    BadTcpServerTooBusy = 0x807D0000
    BadTcpMessageTypeInvalid = 0x807E0000
    BadTcpSecureChannelUnknown = 0x807F0000
    BadTcpMessageTooLarge = 0x80800000
    BadTcpNotEnoughResources = 0x80810000
    BadTcpInternalError = 0x80820000
    BadTcpEndpointUrlInvalid = 0x80830000
    BadRequestInterrupted = 0x80840000
    BadRequestTimeout = 0x80850000
    BadSecureChannelClosed = 0x80860000
    BadSecureChannelTokenUnknown = 0x80870000
    BadSequenceNumberInvalid = 0x80880000
    BadProtocolVersionUnsupported = 0x80BE0000
    BadConfigurationError = 0x80890000
    BadNotConnected = 0x808A0000
    BadDeviceFailure = 0x808B0000
    BadSensorFailure = 0x808C0000
    BadOutOfService = 0x808D0000
    BadDeadbandFilterInvalid = 0x808E0000
    UncertainNoCommunicationLastUsableValue = 0x408F0000
    UncertainLastUsableValue = 0x40900000
    UncertainSubstituteValue = 0x40910000
    UncertainInitialValue = 0x40920000
    UncertainSensorNotAccurate = 0x40930000
    UncertainEngineeringUnitsExceeded = 0x40940000
    UncertainSubNormal = 0x40950000
    GoodLocalOverride = 0x00960000
    BadRefreshInProgress = 0x80970000
    BadConditionAlreadyDisabled = 0x80980000
    BadConditionAlreadyEnabled = 0x80CC0000
    BadConditionDisabled = 0x80990000
    BadEventIdUnknown = 0x809A0000
    BadEventNotAcknowledgeable = 0x80BB0000
    BadDialogNotActive = 0x80CD0000
    BadDialogResponseInvalid = 0x80CE0000
    BadConditionBranchAlreadyAcked = 0x80CF0000
    BadConditionBranchAlreadyConfirmed = 0x80D00000
    BadConditionAlreadyShelved = 0x80D10000
    BadConditionNotShelved = 0x80D20000
    BadShelvingTimeOutOfRange = 0x80D30000
    BadNoData = 0x809B0000
    BadBoundNotFound = 0x80D70000
    BadBoundNotSupported = 0x80D80000
    BadDataLost = 0x809D0000
    BadDataUnavailable = 0x809E0000
    BadEntryExists = 0x809F0000
    BadNoEntryExists = 0x80A00000
    BadTimestampNotSupported = 0x80A10000
    GoodEntryInserted = 0x00A20000
    GoodEntryReplaced = 0x00A30000
    UncertainDataSubNormal = 0x40A40000
    GoodNoData = 0x00A50000
    GoodMoreData = 0x00A60000
    BadAggregateListMismatch = 0x80D40000
    BadAggregateNotSupported = 0x80D50000
    BadAggregateInvalidInputs = 0x80D60000
    BadAggregateConfigurationRejected = 0x80DA0000
    GoodDataIgnored = 0x00D90000
    GoodCommunicationEvent = 0x00A70000
    GoodShutdownEvent = 0x00A80000
    GoodCallAgain = 0x00A90000
    GoodNonCriticalTimeout = 0x00AA0000
    BadInvalidArgument = 0x80AB0000
    BadConnectionRejected = 0x80AC0000
    BadDisconnect = 0x80AD0000
    BadConnectionClosed = 0x80AE0000
    BadInvalidState = 0x80AF0000
    BadEndOfStream = 0x80B00000
    BadNoDataAvailable = 0x80B10000
    BadWaitingForResponse = 0x80B20000
    BadOperationAbandoned = 0x80B30000
    BadExpectedStreamToBlock = 0x80B40000
    BadWouldBlock = 0x80B50000
    BadSyntaxError = 0x80B60000
    BadMaxConnectionsReached = 0x80B70000


def get_name_and_doc(val):
    if val == 0:
        return 'Good', 'The operation completed successfully.'
    elif val == 0x40000000:
        return 'Uncertain', 'The operation completed however its outputs may not be usable.'
    elif val == 0x80000000:
        return 'Bad', 'The operation failed.'
    elif val == 0x80010000:
        return 'BadUnexpectedError', 'An unexpected error occurred.'
    elif val == 0x80020000:
        return 'BadInternalError', 'An internal error occurred as a result of a programming or configuration error.'
    elif val == 0x80030000:
        return 'BadOutOfMemory', 'Not enough memory to complete the operation.'
    elif val == 0x80040000:
        return 'BadResourceUnavailable', 'An operating system resource is not available.'
    elif val == 0x80050000:
        return 'BadCommunicationError', 'A low level communication error occurred.'
    elif val == 0x80060000:
        return 'BadEncodingError', 'Encoding halted because of invalid data in the objects being serialized.'
    elif val == 0x80070000:
        return 'BadDecodingError', 'Decoding halted because of invalid data in the stream.'
    elif val == 0x80080000:
        return 'BadEncodingLimitsExceeded', 'The message encoding/decoding limits imposed by the stack have been exceeded.'
    elif val == 0x80B80000:
        return 'BadRequestTooLarge', 'The request message size exceeds limits set by the server.'
    elif val == 0x80B90000:
        return 'BadResponseTooLarge', 'The response message size exceeds limits set by the client.'
    elif val == 0x80090000:
        return 'BadUnknownResponse', 'An unrecognized response was received from the server.'
    elif val == 0x800A0000:
        return 'BadTimeout', 'The operation timed out.'
    elif val == 0x800B0000:
        return 'BadServiceUnsupported', 'The server does not support the requested service.'
    elif val == 0x800C0000:
        return 'BadShutdown', 'The operation was cancelled because the application is shutting down.'
    elif val == 0x800D0000:
        return 'BadServerNotConnected', 'The operation could not complete because the client is not connected to the server.'
    elif val == 0x800E0000:
        return 'BadServerHalted', 'The server has stopped and cannot process any requests.'
    elif val == 0x800F0000:
        return 'BadNothingToDo', 'There was nothing to do because the client passed a list of operations with no elements.'
    elif val == 0x80100000:
        return 'BadTooManyOperations', 'The request could not be processed because it specified too many operations.'
    elif val == 0x80DB0000:
        return 'BadTooManyMonitoredItems', 'The request could not be processed because there are too many monitored items in the subscription.'
    elif val == 0x80110000:
        return 'BadDataTypeIdUnknown', 'The extension object cannot be (de)serialized because the data type id is not recognized.'
    elif val == 0x80120000:
        return 'BadCertificateInvalid', 'The certificate provided as a parameter is not valid.'
    elif val == 0x80130000:
        return 'BadSecurityChecksFailed', 'An error occurred verifying security.'
    elif val == 0x80140000:
        return 'BadCertificateTimeInvalid', 'The Certificate has expired or is not yet valid.'
    elif val == 0x80150000:
        return 'BadCertificateIssuerTimeInvalid', 'An Issuer Certificate has expired or is not yet valid.'
    elif val == 0x80160000:
        return 'BadCertificateHostNameInvalid', 'The HostName used to connect to a Server does not match a HostName in the Certificate.'
    elif val == 0x80170000:
        return 'BadCertificateUriInvalid', 'The URI specified in the ApplicationDescription does not match the URI in the Certificate.'
    elif val == 0x80180000:
        return 'BadCertificateUseNotAllowed', 'The Certificate may not be used for the requested operation.'
    elif val == 0x80190000:
        return 'BadCertificateIssuerUseNotAllowed', 'The Issuer Certificate may not be used for the requested operation.'
    elif val == 0x801A0000:
        return 'BadCertificateUntrusted', 'The Certificate is not trusted.'
    elif val == 0x801B0000:
        return 'BadCertificateRevocationUnknown', 'It was not possible to determine if the Certificate has been revoked.'
    elif val == 0x801C0000:
        return 'BadCertificateIssuerRevocationUnknown', 'It was not possible to determine if the Issuer Certificate has been revoked.'
    elif val == 0x801D0000:
        return 'BadCertificateRevoked', 'The Certificate has been revoked.'
    elif val == 0x801E0000:
        return 'BadCertificateIssuerRevoked', 'The Issuer Certificate has been revoked.'
    elif val == 0x801F0000:
        return 'BadUserAccessDenied', 'User does not have permission to perform the requested operation.'
    elif val == 0x80200000:
        return 'BadIdentityTokenInvalid', 'The user identity token is not valid.'
    elif val == 0x80210000:
        return 'BadIdentityTokenRejected', 'The user identity token is valid but the server has rejected it.'
    elif val == 0x80220000:
        return 'BadSecureChannelIdInvalid', 'The specified secure channel is no longer valid.'
    elif val == 0x80230000:
        return 'BadInvalidTimestamp', 'The timestamp is outside the range allowed by the server.'
    elif val == 0x80240000:
        return 'BadNonceInvalid', 'The nonce does appear to be not a random value or it is not the correct length.'
    elif val == 0x80250000:
        return 'BadSessionIdInvalid', 'The session id is not valid.'
    elif val == 0x80260000:
        return 'BadSessionClosed', 'The session was closed by the client.'
    elif val == 0x80270000:
        return 'BadSessionNotActivated', 'The session cannot be used because ActivateSession has not been called.'
    elif val == 0x80280000:
        return 'BadSubscriptionIdInvalid', 'The subscription id is not valid.'
    elif val == 0x802A0000:
        return 'BadRequestHeaderInvalid', 'The header for the request is missing or invalid.'
    elif val == 0x802B0000:
        return 'BadTimestampsToReturnInvalid', 'The timestamps to return parameter is invalid.'
    elif val == 0x802C0000:
        return 'BadRequestCancelledByClient', 'The request was cancelled by the client.'
    elif val == 0x002D0000:
        return 'GoodSubscriptionTransferred', 'The subscription was transferred to another session.'
    elif val == 0x002E0000:
        return 'GoodCompletesAsynchronously', 'The processing will complete asynchronously.'
    elif val == 0x002F0000:
        return 'GoodOverload', 'Sampling has slowed down due to resource limitations.'
    elif val == 0x00300000:
        return 'GoodClamped', 'The value written was accepted but was clamped.'
    elif val == 0x80310000:
        return 'BadNoCommunication', 'Communication with the data source is defined, but not established, and there is no last known value available.'
    elif val == 0x80320000:
        return 'BadWaitingForInitialData', 'Waiting for the server to obtain values from the underlying data source.'
    elif val == 0x80330000:
        return 'BadNodeIdInvalid', 'The syntax of the node id is not valid.'
    elif val == 0x80340000:
        return 'BadNodeIdUnknown', 'The node id refers to a node that does not exist in the server address space.'
    elif val == 0x80350000:
        return 'BadAttributeIdInvalid', 'The attribute is not supported for the specified Node.'
    elif val == 0x80360000:
        return 'BadIndexRangeInvalid', 'The syntax of the index range parameter is invalid.'
    elif val == 0x80370000:
        return 'BadIndexRangeNoData', 'No data exists within the range of indexes specified.'
    elif val == 0x80380000:
        return 'BadDataEncodingInvalid', 'The data encoding is invalid.'
    elif val == 0x80390000:
        return 'BadDataEncodingUnsupported', 'The server does not support the requested data encoding for the node.'
    elif val == 0x803A0000:
        return 'BadNotReadable', 'The access level does not allow reading or subscribing to the Node.'
    elif val == 0x803B0000:
        return 'BadNotWritable', 'The access level does not allow writing to the Node.'
    elif val == 0x803C0000:
        return 'BadOutOfRange', 'The value was out of range.'
    elif val == 0x803D0000:
        return 'BadNotSupported', 'The requested operation is not supported.'
    elif val == 0x803E0000:
        return 'BadNotFound', 'A requested item was not found or a search operation ended without success.'
    elif val == 0x803F0000:
        return 'BadObjectDeleted', 'The object cannot be used because it has been deleted.'
    elif val == 0x80400000:
        return 'BadNotImplemented', 'Requested operation is not implemented.'
    elif val == 0x80410000:
        return 'BadMonitoringModeInvalid', 'The monitoring mode is invalid.'
    elif val == 0x80420000:
        return 'BadMonitoredItemIdInvalid', 'The monitoring item id does not refer to a valid monitored item.'
    elif val == 0x80430000:
        return 'BadMonitoredItemFilterInvalid', 'The monitored item filter parameter is not valid.'
    elif val == 0x80440000:
        return 'BadMonitoredItemFilterUnsupported', 'The server does not support the requested monitored item filter.'
    elif val == 0x80450000:
        return 'BadFilterNotAllowed', 'A monitoring filter cannot be used in combination with the attribute specified.'
    elif val == 0x80460000:
        return 'BadStructureMissing', 'A mandatory structured parameter was missing or null.'
    elif val == 0x80470000:
        return 'BadEventFilterInvalid', 'The event filter is not valid.'
    elif val == 0x80480000:
        return 'BadContentFilterInvalid', 'The content filter is not valid.'
    elif val == 0x80C10000:
        return 'BadFilterOperatorInvalid', 'An unregognized operator was provided in a filter.'
    elif val == 0x80C20000:
        return 'BadFilterOperatorUnsupported', 'A valid operator was provided, but the server does not provide support for this filter operator.'
    elif val == 0x80C30000:
        return 'BadFilterOperandCountMismatch', 'The number of operands provided for the filter operator was less then expected for the operand provided.'
    elif val == 0x80490000:
        return 'BadFilterOperandInvalid', 'The operand used in a content filter is not valid.'
    elif val == 0x80C40000:
        return 'BadFilterElementInvalid', 'The referenced element is not a valid element in the content filter.'
    elif val == 0x80C50000:
        return 'BadFilterLiteralInvalid', 'The referenced literal is not a valid value.'
    elif val == 0x804A0000:
        return 'BadContinuationPointInvalid', 'The continuation point provide is longer valid.'
    elif val == 0x804B0000:
        return 'BadNoContinuationPoints', 'The operation could not be processed because all continuation points have been allocated.'
    elif val == 0x804C0000:
        return 'BadReferenceTypeIdInvalid', 'The operation could not be processed because all continuation points have been allocated.'
    elif val == 0x804D0000:
        return 'BadBrowseDirectionInvalid', 'The browse direction is not valid.'
    elif val == 0x804E0000:
        return 'BadNodeNotInView', 'The node is not part of the view.'
    elif val == 0x804F0000:
        return 'BadServerUriInvalid', 'The ServerUri is not a valid URI.'
    elif val == 0x80500000:
        return 'BadServerNameMissing', 'No ServerName was specified.'
    elif val == 0x80510000:
        return 'BadDiscoveryUrlMissing', 'No DiscoveryUrl was specified.'
    elif val == 0x80520000:
        return 'BadSempahoreFileMissing', 'The semaphore file specified by the client is not valid.'
    elif val == 0x80530000:
        return 'BadRequestTypeInvalid', 'The security token request type is not valid.'
    elif val == 0x80540000:
        return 'BadSecurityModeRejected', 'The security mode does not meet the requirements set by the Server.'
    elif val == 0x80550000:
        return 'BadSecurityPolicyRejected', 'The security policy does not meet the requirements set by the Server.'
    elif val == 0x80560000:
        return 'BadTooManySessions', 'The server has reached its maximum number of sessions.'
    elif val == 0x80570000:
        return 'BadUserSignatureInvalid', 'The user token signature is missing or invalid.'
    elif val == 0x80580000:
        return 'BadApplicationSignatureInvalid', 'The signature generated with the client certificate is missing or invalid.'
    elif val == 0x80590000:
        return 'BadNoValidCertificates', 'The client did not provide at least one software certificate that is valid and meets the profile requirements for the server.'
    elif val == 0x80C60000:
        return 'BadIdentityChangeNotSupported', 'The Server does not support changing the user identity assigned to the session.'
    elif val == 0x805A0000:
        return 'BadRequestCancelledByRequest', 'The request was cancelled by the client with the Cancel service.'
    elif val == 0x805B0000:
        return 'BadParentNodeIdInvalid', 'The parent node id does not to refer to a valid node.'
    elif val == 0x805C0000:
        return 'BadReferenceNotAllowed', 'The reference could not be created because it violates constraints imposed by the data model.'
    elif val == 0x805D0000:
        return 'BadNodeIdRejected', 'The requested node id was reject because it was either invalid or server does not allow node ids to be specified by the client.'
    elif val == 0x805E0000:
        return 'BadNodeIdExists', 'The requested node id is already used by another node.'
    elif val == 0x805F0000:
        return 'BadNodeClassInvalid', 'The node class is not valid.'
    elif val == 0x80600000:
        return 'BadBrowseNameInvalid', 'The browse name is invalid.'
    elif val == 0x80610000:
        return 'BadBrowseNameDuplicated', 'The browse name is not unique among nodes that share the same relationship with the parent.'
    elif val == 0x80620000:
        return 'BadNodeAttributesInvalid', 'The node attributes are not valid for the node class.'
    elif val == 0x80630000:
        return 'BadTypeDefinitionInvalid', 'The type definition node id does not reference an appropriate type node.'
    elif val == 0x80640000:
        return 'BadSourceNodeIdInvalid', 'The source node id does not reference a valid node.'
    elif val == 0x80650000:
        return 'BadTargetNodeIdInvalid', 'The target node id does not reference a valid node.'
    elif val == 0x80660000:
        return 'BadDuplicateReferenceNotAllowed', 'The reference type between the nodes is already defined.'
    elif val == 0x80670000:
        return 'BadInvalidSelfReference', 'The server does not allow this type of self reference on this node.'
    elif val == 0x80680000:
        return 'BadReferenceLocalOnly', 'The reference type is not valid for a reference to a remote server.'
    elif val == 0x80690000:
        return 'BadNoDeleteRights', 'The server will not allow the node to be deleted.'
    elif val == 0x40BC0000:
        return 'UncertainReferenceNotDeleted', 'The server was not able to delete all target references.'
    elif val == 0x806A0000:
        return 'BadServerIndexInvalid', 'The server index is not valid.'
    elif val == 0x806B0000:
        return 'BadViewIdUnknown', 'The view id does not refer to a valid view node.'
    elif val == 0x80C90000:
        return 'BadViewTimestampInvalid', 'The view timestamp is not available or not supported.'
    elif val == 0x80CA0000:
        return 'BadViewParameterMismatch', 'The view parameters are not consistent with each other.'
    elif val == 0x80CB0000:
        return 'BadViewVersionInvalid', 'The view version is not available or not supported.'
    elif val == 0x40C00000:
        return 'UncertainNotAllNodesAvailable', 'The list of references may not be complete because the underlying system is not available.'
    elif val == 0x00BA0000:
        return 'GoodResultsMayBeIncomplete', 'The server should have followed a reference to a node in a remote server but did not. The result set may be incomplete.'
    elif val == 0x80C80000:
        return 'BadNotTypeDefinition', 'The provided Nodeid was not a type definition nodeid.'
    elif val == 0x406C0000:
        return 'UncertainReferenceOutOfServer', 'One of the references to follow in the relative path references to a node in the address space in another server.'
    elif val == 0x806D0000:
        return 'BadTooManyMatches', 'The requested operation has too many matches to return.'
    elif val == 0x806E0000:
        return 'BadQueryTooComplex', 'The requested operation requires too many resources in the server.'
    elif val == 0x806F0000:
        return 'BadNoMatch', 'The requested operation has no match to return.'
    elif val == 0x80700000:
        return 'BadMaxAgeInvalid', 'The max age parameter is invalid.'
    elif val == 0x80710000:
        return 'BadHistoryOperationInvalid', 'The history details parameter is not valid.'
    elif val == 0x80720000:
        return 'BadHistoryOperationUnsupported', 'The server does not support the requested operation.'
    elif val == 0x80BD0000:
        return 'BadInvalidTimestampArgument', 'The defined timestamp to return was invalid.'
    elif val == 0x80730000:
        return 'BadWriteNotSupported', 'The server not does support writing the combination of value, status and timestamps provided.'
    elif val == 0x80740000:
        return 'BadTypeMismatch', 'The value supplied for the attribute is not of the same type as the attribute"s value.'
    elif val == 0x80750000:
        return 'BadMethodInvalid', 'The method id does not refer to a method for the specified object.'
    elif val == 0x80760000:
        return 'BadArgumentsMissing', 'The client did not specify all of the input arguments for the method.'
    elif val == 0x80770000:
        return 'BadTooManySubscriptions', 'The server has reached its  maximum number of subscriptions.'
    elif val == 0x80780000:
        return 'BadTooManyPublishRequests', 'The server has reached the maximum number of queued publish requests.'
    elif val == 0x80790000:
        return 'BadNoSubscription', 'There is no subscription available for this session.'
    elif val == 0x807A0000:
        return 'BadSequenceNumberUnknown', 'The sequence number is unknown to the server.'
    elif val == 0x807B0000:
        return 'BadMessageNotAvailable', 'The requested notification message is no longer available.'
    elif val == 0x807C0000:
        return 'BadInsufficientClientProfile', 'The Client of the current Session does not support one or more Profiles that are necessary for the Subscription.'
    elif val == 0x80BF0000:
        return 'BadStateNotActive', 'The sub-state machine is not currently active.'
    elif val == 0x807D0000:
        return 'BadTcpServerTooBusy', 'The server cannot process the request because it is too busy.'
    elif val == 0x807E0000:
        return 'BadTcpMessageTypeInvalid', 'The type of the message specified in the header invalid.'
    elif val == 0x807F0000:
        return 'BadTcpSecureChannelUnknown', 'The SecureChannelId and/or TokenId are not currently in use.'
    elif val == 0x80800000:
        return 'BadTcpMessageTooLarge', 'The size of the message specified in the header is too large.'
    elif val == 0x80810000:
        return 'BadTcpNotEnoughResources', 'There are not enough resources to process the request.'
    elif val == 0x80820000:
        return 'BadTcpInternalError', 'An internal error occurred.'
    elif val == 0x80830000:
        return 'BadTcpEndpointUrlInvalid', 'The Server does not recognize the QueryString specified.'
    elif val == 0x80840000:
        return 'BadRequestInterrupted', 'The request could not be sent because of a network interruption.'
    elif val == 0x80850000:
        return 'BadRequestTimeout', 'Timeout occurred while processing the request.'
    elif val == 0x80860000:
        return 'BadSecureChannelClosed', 'The secure channel has been closed.'
    elif val == 0x80870000:
        return 'BadSecureChannelTokenUnknown', 'The token has expired or is not recognized.'
    elif val == 0x80880000:
        return 'BadSequenceNumberInvalid', 'The sequence number is not valid.'
    elif val == 0x80BE0000:
        return 'BadProtocolVersionUnsupported', 'The applications do not have compatible protocol versions.'
    elif val == 0x80890000:
        return 'BadConfigurationError', 'There is a problem with the configuration that affects the usefulness of the value.'
    elif val == 0x808A0000:
        return 'BadNotConnected', 'The variable should receive its value from another variable, but has never been configured to do so.'
    elif val == 0x808B0000:
        return 'BadDeviceFailure', 'There has been a failure in the device/data source that generates the value that has affected the value.'
    elif val == 0x808C0000:
        return 'BadSensorFailure', 'There has been a failure in the sensor from which the value is derived by the device/data source.'
    elif val == 0x808D0000:
        return 'BadOutOfService', 'The source of the data is not operational.'
    elif val == 0x808E0000:
        return 'BadDeadbandFilterInvalid', 'The deadband filter is not valid.'
    elif val == 0x408F0000:
        return 'UncertainNoCommunicationLastUsableValue', 'Communication to the data source has failed. The variable value is the last value that had a good quality.'
    elif val == 0x40900000:
        return 'UncertainLastUsableValue', 'Whatever was updating this value has stopped doing so.'
    elif val == 0x40910000:
        return 'UncertainSubstituteValue', 'The value is an operational value that was manually overwritten.'
    elif val == 0x40920000:
        return 'UncertainInitialValue', 'The value is an initial value for a variable that normally receives its value from another variable.'
    elif val == 0x40930000:
        return 'UncertainSensorNotAccurate', 'The value is at one of the sensor limits.'
    elif val == 0x40940000:
        return 'UncertainEngineeringUnitsExceeded', 'The value is outside of the range of values defined for this parameter.'
    elif val == 0x40950000:
        return 'UncertainSubNormal', 'The value is derived from multiple sources and has less than the required number of Good sources.'
    elif val == 0x00960000:
        return 'GoodLocalOverride', 'The value has been overridden.'
    elif val == 0x80970000:
        return 'BadRefreshInProgress', 'This Condition refresh failed, a Condition refresh operation is already in progress.'
    elif val == 0x80980000:
        return 'BadConditionAlreadyDisabled', 'This condition has already been disabled.'
    elif val == 0x80CC0000:
        return 'BadConditionAlreadyEnabled', 'This condition has already been enabled.'
    elif val == 0x80990000:
        return 'BadConditionDisabled', 'Property not available, this condition is disabled.'
    elif val == 0x809A0000:
        return 'BadEventIdUnknown', 'The specified event id is not recognized.'
    elif val == 0x80BB0000:
        return 'BadEventNotAcknowledgeable', 'The event cannot be acknowledged.'
    elif val == 0x80CD0000:
        return 'BadDialogNotActive', 'The dialog condition is not active.'
    elif val == 0x80CE0000:
        return 'BadDialogResponseInvalid', 'The response is not valid for the dialog.'
    elif val == 0x80CF0000:
        return 'BadConditionBranchAlreadyAcked', 'The condition branch has already been acknowledged.'
    elif val == 0x80D00000:
        return 'BadConditionBranchAlreadyConfirmed', 'The condition branch has already been confirmed.'
    elif val == 0x80D10000:
        return 'BadConditionAlreadyShelved', 'The condition has already been shelved.'
    elif val == 0x80D20000:
        return 'BadConditionNotShelved', 'The condition is not currently shelved.'
    elif val == 0x80D30000:
        return 'BadShelvingTimeOutOfRange', 'The shelving time not within an acceptable range.'
    elif val == 0x809B0000:
        return 'BadNoData', 'No data exists for the requested time range or event filter.'
    elif val == 0x80D70000:
        return 'BadBoundNotFound', 'No data found to provide upper or lower bound value.'
    elif val == 0x80D80000:
        return 'BadBoundNotSupported', 'The server cannot retrieve a bound for the variable.'
    elif val == 0x809D0000:
        return 'BadDataLost', 'Data is missing due to collection started/stopped/lost.'
    elif val == 0x809E0000:
        return 'BadDataUnavailable', 'Expected data is unavailable for the requested time range due to an un-mounted volume, an off-line archive or tape, or similar reason for temporary unavailability.'
    elif val == 0x809F0000:
        return 'BadEntryExists', 'The data or event was not successfully inserted because a matching entry exists.'
    elif val == 0x80A00000:
        return 'BadNoEntryExists', 'The data or event was not successfully updated because no matching entry exists.'
    elif val == 0x80A10000:
        return 'BadTimestampNotSupported', 'The client requested history using a timestamp format the server does not support (i.e requested ServerTimestamp when server only supports SourceTimestamp).'
    elif val == 0x00A20000:
        return 'GoodEntryInserted', 'The data or event was successfully inserted into the historical database.'
    elif val == 0x00A30000:
        return 'GoodEntryReplaced', 'The data or event field was successfully replaced in the historical database.'
    elif val == 0x40A40000:
        return 'UncertainDataSubNormal', 'The value is derived from multiple values and has less than the required number of Good values.'
    elif val == 0x00A50000:
        return 'GoodNoData', 'No data exists for the requested time range or event filter.'
    elif val == 0x00A60000:
        return 'GoodMoreData', 'The data or event field was successfully replaced in the historical database.'
    elif val == 0x80D40000:
        return 'BadAggregateListMismatch', 'The requested number of Aggregates does not match the requested number of NodeIds.'
    elif val == 0x80D50000:
        return 'BadAggregateNotSupported', 'The requested Aggregate is not support by the server.'
    elif val == 0x80D60000:
        return 'BadAggregateInvalidInputs', 'The aggregate value could not be derived due to invalid data inputs.'
    elif val == 0x80DA0000:
        return 'BadAggregateConfigurationRejected', 'The aggregate configuration is not valid for specified node.'
    elif val == 0x00D90000:
        return 'GoodDataIgnored', 'The request pecifies fields which are not valid for the EventType or cannot be saved by the historian.'
    elif val == 0x00A70000:
        return 'GoodCommunicationEvent', 'The communication layer has raised an event.'
    elif val == 0x00A80000:
        return 'GoodShutdownEvent', 'The system is shutting down.'
    elif val == 0x00A90000:
        return 'GoodCallAgain', 'The operation is not finished and needs to be called again.'
    elif val == 0x00AA0000:
        return 'GoodNonCriticalTimeout', 'A non-critical timeout occurred.'
    elif val == 0x80AB0000:
        return 'BadInvalidArgument', 'One or more arguments are invalid.'
    elif val == 0x80AC0000:
        return 'BadConnectionRejected', 'Could not establish a network connection to remote server.'
    elif val == 0x80AD0000:
        return 'BadDisconnect', 'The server has disconnected from the client.'
    elif val == 0x80AE0000:
        return 'BadConnectionClosed', 'The network connection has been closed.'
    elif val == 0x80AF0000:
        return 'BadInvalidState', 'The operation cannot be completed because the object is closed, uninitialized or in some other invalid state.'
    elif val == 0x80B00000:
        return 'BadEndOfStream', 'Cannot move beyond end of the stream.'
    elif val == 0x80B10000:
        return 'BadNoDataAvailable', 'No data is currently available for reading from a non-blocking stream.'
    elif val == 0x80B20000:
        return 'BadWaitingForResponse', 'The asynchronous operation is waiting for a response.'
    elif val == 0x80B30000:
        return 'BadOperationAbandoned', 'The asynchronous operation was abandoned by the caller.'
    elif val == 0x80B40000:
        return 'BadExpectedStreamToBlock', 'The stream did not return all data requested (possibly because it is a non-blocking stream).'
    elif val == 0x80B50000:
        return 'BadWouldBlock', 'Non blocking behaviour is required and the operation would block.'
    elif val == 0x80B60000:
        return 'BadSyntaxError', 'A value had an invalid syntax.'
    elif val == 0x80B70000:
        return 'BadMaxConnectionsReached', 'The operation could not be finished because all available connections are in use.'
    else:
        return 'UknownUaError', 'Unknown StatusCode value: {}'.format(val)
