/*
 * Copyright 2010-2020 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.ir.backend.py

import org.jetbrains.kotlin.builtins.PrimitiveType
import org.jetbrains.kotlin.incremental.components.NoLookupLocation
import org.jetbrains.kotlin.ir.IrBuiltIns
import org.jetbrains.kotlin.ir.declarations.IrFunction
import org.jetbrains.kotlin.ir.declarations.IrProperty
import org.jetbrains.kotlin.ir.declarations.IrSimpleFunction
import org.jetbrains.kotlin.ir.symbols.IrSimpleFunctionSymbol
import org.jetbrains.kotlin.ir.types.isLong
import org.jetbrains.kotlin.ir.util.constructors
import org.jetbrains.kotlin.ir.util.findDeclaration
import org.jetbrains.kotlin.name.FqName
import org.jetbrains.kotlin.name.Name
import org.jetbrains.kotlin.psi2ir.findSingleFunction
import org.jetbrains.kotlin.util.capitalizeDecapitalize.toLowerCaseAsciiOnly
import java.util.*

class JsIntrinsics(private val irBuiltIns: IrBuiltIns, val context: JsIrBackendContext) {

    // TODO: Should we drop operator intrinsics in favor of IrDynamicOperatorExpression?

    // Equality operations:

    val jsEqeq = getInternalFunction("jsEqeq")
    val jsNotEq = getInternalFunction("jsNotEq")
    val jsEqeqeq = getInternalFunction("jsEqeqeq")
    val jsNotEqeq = getInternalFunction("jsNotEqeq")

    val jsGt = getInternalFunction("jsGt")
    val jsGtEq = getInternalFunction("jsGtEq")
    val jsLt = getInternalFunction("jsLt")
    val jsLtEq = getInternalFunction("jsLtEq")


    // Unary operations:

    val jsNot = getInternalFunction("jsNot")

    val jsUnaryPlus = getInternalFunction("jsUnaryPlus")
    val jsUnaryMinus = getInternalFunction("jsUnaryMinus")

    // Binary operations:

    val jsPlus = getInternalFunction("jsPlus")
    val jsMinus = getInternalFunction("jsMinus")
    val jsMult = getInternalFunction("jsMult")
    val jsDiv = getInternalFunction("jsDiv")
    val jsMod = getInternalFunction("jsMod")

    val jsOr = getInternalFunction("jsOr")

    // Bit operations:

    val jsBitAnd = getInternalFunction("jsBitAnd")
    val jsBitOr = getInternalFunction("jsBitOr")
    val jsBitXor = getInternalFunction("jsBitXor")
    val jsBitNot = getInternalFunction("jsBitNot")

    val jsBitShiftR = getInternalFunction("jsBitShiftR")
    val jsBitShiftRU = getInternalFunction("jsBitShiftRU")
    val jsBitShiftL = getInternalFunction("jsBitShiftL")

    // Type checks:

    val jsInstanceOf = getInternalFunction("jsInstanceOfIntrinsic")
    val jsTypeOf = getInternalFunction("jsTypeOf")

    // Number conversions:

    val jsNumberToByte = getInternalFunction("numberToByte")
    val jsNumberToDouble = getInternalFunction("numberToDouble")
    val jsNumberToInt = getInternalFunction("numberToInt")
    val jsNumberToShort = getInternalFunction("numberToShort")
    val jsNumberToLong = getInternalFunction("numberToLong")
    val jsNumberToChar = getInternalFunction("numberToChar")
    val jsToLong = getInternalFunction("toLong")


    // RTTI:

    val isInterfaceSymbol = getInternalFunction("isInterface")
    val isArraySymbol = getInternalFunction("isArray")
    val isObjectSymbol = getInternalFunction("isObject")
    val isSuspendFunctionSymbol = getInternalFunction("isSuspendFunction")

    val isNumberSymbol = getInternalFunction("isNumber")
    val isComparableSymbol = getInternalFunction("isComparable")
    val isCharSequenceSymbol = getInternalFunction("isCharSequence")

    val isPrimitiveArray = mapOf(
        PrimitiveType.BOOLEAN to getInternalFunction("isBooleanArray"),
        PrimitiveType.BYTE to getInternalFunction("isByteArray"),
        PrimitiveType.SHORT to getInternalFunction("isShortArray"),
        PrimitiveType.CHAR to getInternalFunction("isCharArray"),
        PrimitiveType.INT to getInternalFunction("isIntArray"),
        PrimitiveType.FLOAT to getInternalFunction("isFloatArray"),
        PrimitiveType.LONG to getInternalFunction("isLongArray"),
        PrimitiveType.DOUBLE to getInternalFunction("isDoubleArray")
    )


    // Enum

    val enumValueOfIntrinsic = getInternalFunction("enumValueOfIntrinsic")
    val enumValuesIntrinsic = getInternalFunction("enumValuesIntrinsic")


    // Other:

    val jsObjectCreate = getInternalFunction("objectCreate") // Object.create
    val jsCode = getInternalFunction("js") // js("<code>")
    val jsHashCode = getInternalFunction("hashCode")
    val jsGetNumberHashCode = getInternalFunction("getNumberHashCode")
    val jsGetObjectHashCode = getInternalFunction("getObjectHashCode")
    val jsGetStringHashCode = getInternalFunction("getStringHashCode")
    val jsToString = getInternalFunction("toString")
    val jsAnyToString = getInternalFunction("anyToString")
    val jsCompareTo = getInternalFunction("compareTo")
    val jsEquals = getInternalFunction("equals")
    val jsConstruct = getInternalFunction("construct")
    val jsNewTarget = getInternalFunction("jsNewTarget")
    val jsEmptyObject = getInternalFunction("emptyObject")
    val jsOpenInitializerBox = getInternalFunction("openInitializerBox")
    val es6DefaultType = getInternalFunction("DefaultType")

    val jsImul = getInternalFunction("imul")

    val jsNumberRangeToNumber = getInternalFunction("numberRangeToNumber")
    val jsNumberRangeToLong = getInternalFunction("numberRangeToLong")

    private fun getMethod(fqClassName: String, function: String) = context
        .getClass(FqName(fqClassName))
        .unsubstitutedMemberScope
        .findSingleFunction(Name.identifier(function))
        .let(context.symbolTable::referenceSimpleFunction)

    private fun getMethods(fqClassName: String, function: String) = context
        .getClass(FqName(fqClassName))
        .unsubstitutedMemberScope
        .getContributedFunctions(Name.identifier(function), NoLookupLocation.FROM_BACKEND)
        .map(context.symbolTable::referenceSimpleFunction)

    val byteToByte = getMethod("kotlin.Byte", "toByte")
    val byteToShort = getMethod("kotlin.Byte", "toShort")
    val byteToInt = getMethod("kotlin.Byte", "toInt")
    val byteToLong = getMethod("kotlin.Byte", "toLong")
    val shortToByte = getMethod("kotlin.Short", "toByte")
    val shortToShort = getMethod("kotlin.Short", "toShort")
    val shortToInt = getMethod("kotlin.Short", "toInt")
    val shortToLong = getMethod("kotlin.Short", "toLong")
    val intToByte = getMethod("kotlin.Int", "toByte")
    val intToShort = getMethod("kotlin.Int", "toShort")
    val intToInt = getMethod("kotlin.Int", "toInt")
    val intToLong = getMethod("kotlin.Int", "toLong")
    val longToByte = getMethod("kotlin.Long", "toByte")
    val longToShort = getMethod("kotlin.Long", "toShort")
    val longToInt = getMethod("kotlin.Long", "toInt")
    val longToLong = getMethod("kotlin.Long", "toLong")

    val longPlus = getMethods("kotlin.Long", "plus")
    val longMinus = getMethods("kotlin.Long", "minus")
    val longMult = getMethods("kotlin.Long", "times")
    val longDiv = getMethods("kotlin.Long", "div")
    val longMod = getMethods("kotlin.Long", "mod")
    val longAnd = getMethods("kotlin.Long", "and")
    val longOr = getMethods("kotlin.Long", "or")
    val longXor = getMethods("kotlin.Long", "xor")
    val longInv = getMethod("kotlin.Long", "inv")
    val longShl = getMethods("kotlin.Long", "shl")
    val longShr = getMethods("kotlin.Long", "shr")
    val longUshr = getMethods("kotlin.Long", "ushr")
    val longEquals = getMethods("kotlin.Long", "equals")

    val longClassSymbol = getInternalClassWithoutPackage("kotlin.Long")

    val longToDouble = context.symbolTable.referenceSimpleFunction(
        context.getClass(FqName("kotlin.Long")).unsubstitutedMemberScope.findSingleFunction(
            Name.identifier("toDouble")
        )
    )
    val longToFloat = context.symbolTable.referenceSimpleFunction(
        context.getClass(FqName("kotlin.Long")).unsubstitutedMemberScope.findSingleFunction(
            Name.identifier("toFloat")
        )
    )

    val longCompareToLong: IrSimpleFunction = longClassSymbol.owner.findDeclaration<IrSimpleFunction> {
        it.name == Name.identifier("compareTo") && it.valueParameters[0].type.isLong()
    }!!

    val charClassSymbol = getInternalClassWithoutPackage("kotlin.Char")
    val charConstructor = charClassSymbol.constructors.single().owner

    val stringClassSymbol = getInternalClassWithoutPackage("kotlin.String")
    val stringConstructorSymbol = stringClassSymbol.constructors.single()

    val anyClassSymbol = getInternalClassWithoutPackage("kotlin.Any")
    val anyConstructorSymbol = anyClassSymbol.constructors.single()

    val jsObjectClassSymbol = getInternalClassWithoutPackage("kotlin.js.JsObject")
    val jsObjectConstructorSymbol by context.lazy2 { jsObjectClassSymbol.constructors.single() }

    val uByteClassSymbol by context.lazy2 { getInternalClassWithoutPackage("kotlin.UByte") }
    val uShortClassSymbol by context.lazy2 { getInternalClassWithoutPackage("kotlin.UShort") }
    val uIntClassSymbol by context.lazy2 { getInternalClassWithoutPackage("kotlin.UInt") }
    val uLongClassSymbol by context.lazy2 { getInternalClassWithoutPackage("kotlin.ULong") }

    val unreachable = getInternalFunction("unreachable")

    val returnIfSuspended = getInternalFunction("returnIfSuspended")

    // Arrays:
    val array get() = irBuiltIns.arrayClass

    val primitiveArrays get() = irBuiltIns.primitiveArraysToPrimitiveTypes

    val jsArrayLength = getInternalFunction("jsArrayLength")
    val jsArrayGet = getInternalFunction("jsArrayGet")
    val jsArraySet = getInternalFunction("jsArraySet")

    val jsArrayIteratorFunction = getInternalFunction("arrayIterator")

    val jsPrimitiveArrayIteratorFunctions =
        PrimitiveType.values().associate { it to getInternalFunction("${it.typeName.asString().toLowerCaseAsciiOnly()}ArrayIterator") }

    val arrayLiteral = getInternalFunction("arrayLiteral")

    val primitiveToTypedArrayMap = EnumMap(
        mapOf(
            PrimitiveType.BYTE to "Int8",
            PrimitiveType.SHORT to "Int16",
            PrimitiveType.INT to "Int32",
            PrimitiveType.FLOAT to "Float32",
            PrimitiveType.DOUBLE to "Float64"
        )
    )

    val createKType = getInternalWithoutPackageOrNull("createKType")
    val createDynamicKType = getInternalWithoutPackageOrNull("createDynamicKType")
    val createKTypeParameter = getInternalWithoutPackageOrNull("createKTypeParameter")
    val getStarKTypeProjection = getInternalWithoutPackageOrNull("getStarKTypeProjection")
    val createCovariantKTypeProjection = getInternalWithoutPackageOrNull("createCovariantKTypeProjection")
    val createInvariantKTypeProjection = getInternalWithoutPackageOrNull("createInvariantKTypeProjection")
    val createContravariantKTypeProjection = getInternalWithoutPackageOrNull("createContravariantKTypeProjection")

    val primitiveToSizeConstructor =
        PrimitiveType.values().associate { type ->
            type to (primitiveToTypedArrayMap[type]?.let {
                getInternalFunction("${it.toLowerCaseAsciiOnly()}Array")
            } ?: getInternalFunction("${type.typeName.asString().toLowerCaseAsciiOnly()}Array"))
        }

    val primitiveToLiteralConstructor =
        PrimitiveType.values().associate { type ->
            type to (primitiveToTypedArrayMap[type]?.let {
                getInternalFunction("${it.toLowerCaseAsciiOnly()}ArrayOf")
            } ?: getInternalFunction("${type.typeName.asString().toLowerCaseAsciiOnly()}ArrayOf"))
        }

    val arrayConcat = getInternalWithoutPackage("arrayConcat")

    val primitiveArrayConcat = getInternalWithoutPackage("primitiveArrayConcat")
    val taggedArrayCopy = getInternalWithoutPackage("taggedArrayCopy")

    val jsArraySlice = getInternalFunction("slice")

    val jsBind = getInternalFunction("jsBind")

    // TODO move to IntrinsifyCallsLowering
    val doNotIntrinsifyAnnotationSymbol = context.symbolTable.referenceClass(context.getJsInternalClass("DoNotIntrinsify"))

    // TODO move CharSequence-related stiff to IntrinsifyCallsLowering
    val charSequenceClassSymbol = context.symbolTable.referenceClass(context.getClass(FqName("kotlin.CharSequence")))
    val charSequenceLengthPropertyGetterSymbol by context.lazy2 {
        with(charSequenceClassSymbol.owner.declarations) {
            filterIsInstance<IrProperty>().firstOrNull { it.name.asString() == "length" }?.getter ?:
            filterIsInstance<IrFunction>().first { it.name.asString() == "<get-length>" }
        }.symbol
    }
    val charSequenceGetFunctionSymbol by context.lazy2 {
        charSequenceClassSymbol.owner.declarations.filterIsInstance<IrFunction>().single { it.name.asString() == "get" }.symbol
    }
    val charSequenceSubSequenceFunctionSymbol by context.lazy2 {
        charSequenceClassSymbol.owner.declarations.filterIsInstance<IrFunction>().single { it.name.asString() == "subSequence" }.symbol
    }


    val jsCharSequenceGet = getInternalFunction("charSequenceGet")
    val jsCharSequenceLength = getInternalFunction("charSequenceLength")
    val jsCharSequenceSubSequence = getInternalFunction("charSequenceSubSequence")

    val jsBoxIntrinsic = getInternalFunction("boxIntrinsic")
    val jsUnboxIntrinsic = getInternalFunction("unboxIntrinsic")

    val captureStack = getInternalFunction("captureStack")

    val createSharedBox = getInternalFunction("sharedBoxCreate")
    val readSharedBox = getInternalFunction("sharedBoxRead")
    val writeSharedBox = getInternalFunction("sharedBoxWrite")

    val jsUndefined = getInternalFunction("jsUndefined")

    // Helpers:

    private fun getInternalFunction(name: String) =
        context.symbolTable.referenceSimpleFunction(context.getJsInternalFunction(name))

    private fun getInternalWithoutPackage(name: String) =
        context.symbolTable.referenceSimpleFunction(context.getFunctions(FqName(name)).single())

    private fun getInternalWithoutPackageOrNull(name: String): IrSimpleFunctionSymbol? {
        val descriptor = context.getFunctions(FqName(name)).singleOrNull() ?: return null
        return context.symbolTable.referenceSimpleFunction(descriptor)
    }

    private fun getInternalClassWithoutPackage(fqName: String) =
        context.symbolTable.referenceClass(context.getClass(FqName(fqName)))
}
