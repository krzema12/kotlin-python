/*
 * Copyright 2010-2021 JetBrains s.r.o. and Kotlin Programming Language contributors.
 * Use of this source code is governed by the Apache 2.0 license that can be found in the license/LICENSE.txt file.
 */

package org.jetbrains.kotlin.idea.fir.low.level.api;

import com.intellij.testFramework.TestDataPath;
import org.jetbrains.kotlin.test.util.KtTestUtil;
import org.jetbrains.kotlin.test.TestMetadata;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

import java.io.File;
import java.util.regex.Pattern;

/** This class is generated by {@link GenerateNewCompilerTests.kt}. DO NOT MODIFY MANUALLY */
@SuppressWarnings("all")
@TestMetadata("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir")
@TestDataPath("$PROJECT_ROOT")
public class GetOrBuildFirTestGenerated extends AbstractGetOrBuildFirTest {
    @Test
    public void testAllFilesPresentInGetOrBuildFir() throws Exception {
        KtTestUtil.assertAllTestsPresentByMetadataWithExcluded(this.getClass(), new File("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir"), Pattern.compile("^(.+)\\.kt$"), null, true);
    }

    @Nested
    @TestMetadata("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/annotations")
    @TestDataPath("$PROJECT_ROOT")
    public class Annotations {
        @Test
        public void testAllFilesPresentInAnnotations() throws Exception {
            KtTestUtil.assertAllTestsPresentByMetadataWithExcluded(this.getClass(), new File("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/annotations"), Pattern.compile("^(.+)\\.kt$"), null, true);
        }

        @Test
        @TestMetadata("annotationApplicationArgument.kt")
        public void testAnnotationApplicationArgument() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/annotations/annotationApplicationArgument.kt");
        }

        @Test
        @TestMetadata("annotationApplicationArgumentList.kt")
        public void testAnnotationApplicationArgumentList() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/annotations/annotationApplicationArgumentList.kt");
        }

        @Test
        @TestMetadata("annotationApplicationCallExpression.kt")
        public void testAnnotationApplicationCallExpression() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/annotations/annotationApplicationCallExpression.kt");
        }

        @Test
        @TestMetadata("annotationApplicationVarargArgument.kt")
        public void testAnnotationApplicationVarargArgument() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/annotations/annotationApplicationVarargArgument.kt");
        }

        @Test
        @TestMetadata("annotationApplicationWithArguments.kt")
        public void testAnnotationApplicationWithArguments() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/annotations/annotationApplicationWithArguments.kt");
        }

        @Test
        @TestMetadata("fileAnnotation.kt")
        public void testFileAnnotation() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/annotations/fileAnnotation.kt");
        }
    }

    @Nested
    @TestMetadata("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/calls")
    @TestDataPath("$PROJECT_ROOT")
    public class Calls {
        @Test
        public void testAllFilesPresentInCalls() throws Exception {
            KtTestUtil.assertAllTestsPresentByMetadataWithExcluded(this.getClass(), new File("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/calls"), Pattern.compile("^(.+)\\.kt$"), null, true);
        }

        @Test
        @TestMetadata("callArgument.kt")
        public void testCallArgument() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/calls/callArgument.kt");
        }

        @Test
        @TestMetadata("calllTypeArguments.kt")
        public void testCalllTypeArguments() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/calls/calllTypeArguments.kt");
        }

        @Test
        @TestMetadata("constructorDelegationSuperCall.kt")
        public void testConstructorDelegationSuperCall() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/calls/constructorDelegationSuperCall.kt");
        }

        @Test
        @TestMetadata("constructorDelegationThisCall.kt")
        public void testConstructorDelegationThisCall() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/calls/constructorDelegationThisCall.kt");
        }

        @Test
        @TestMetadata("functionCallArgumentList.kt")
        public void testFunctionCallArgumentList() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/calls/functionCallArgumentList.kt");
        }

        @Test
        @TestMetadata("invokeCallArgumentList.kt")
        public void testInvokeCallArgumentList() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/calls/invokeCallArgumentList.kt");
        }

        @Test
        @TestMetadata("qualifiedCallSelector.kt")
        public void testQualifiedCallSelector() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/calls/qualifiedCallSelector.kt");
        }

        @Test
        @TestMetadata("qualifiedWholeCall.kt")
        public void testQualifiedWholeCall() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/calls/qualifiedWholeCall.kt");
        }
    }

    @Nested
    @TestMetadata("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/declarations")
    @TestDataPath("$PROJECT_ROOT")
    public class Declarations {
        @Test
        public void testAllFilesPresentInDeclarations() throws Exception {
            KtTestUtil.assertAllTestsPresentByMetadataWithExcluded(this.getClass(), new File("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/declarations"), Pattern.compile("^(.+)\\.kt$"), null, true);
        }

        @Test
        @TestMetadata("propertyDelegate.kt")
        public void testPropertyDelegate() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/declarations/propertyDelegate.kt");
        }

        @Test
        @TestMetadata("propertyDelegateExpression.kt")
        public void testPropertyDelegateExpression() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/declarations/propertyDelegateExpression.kt");
        }
    }

    @Nested
    @TestMetadata("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions")
    @TestDataPath("$PROJECT_ROOT")
    public class Expressions {
        @Test
        public void testAllFilesPresentInExpressions() throws Exception {
            KtTestUtil.assertAllTestsPresentByMetadataWithExcluded(this.getClass(), new File("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions"), Pattern.compile("^(.+)\\.kt$"), null, true);
        }

        @Test
        @TestMetadata("arrayAccessExpression.kt")
        public void testArrayAccessExpression() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/arrayAccessExpression.kt");
        }

        @Test
        @TestMetadata("asExpression.kt")
        public void testAsExpression() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/asExpression.kt");
        }

        @Test
        @TestMetadata("binaryExpression.kt")
        public void testBinaryExpression() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/binaryExpression.kt");
        }

        @Test
        @TestMetadata("binaryExpressionOperator.kt")
        public void testBinaryExpressionOperator() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/binaryExpressionOperator.kt");
        }

        @Test
        @TestMetadata("blockExpression.kt")
        public void testBlockExpression() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/blockExpression.kt");
        }

        @Test
        @TestMetadata("boolLiteral.kt")
        public void testBoolLiteral() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/boolLiteral.kt");
        }

        @Test
        @TestMetadata("classAccessExpression.kt")
        public void testClassAccessExpression() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/classAccessExpression.kt");
        }

        @Test
        @TestMetadata("forExpression.kt")
        public void testForExpression() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/forExpression.kt");
        }

        @Test
        @TestMetadata("forExpressionRange.kt")
        public void testForExpressionRange() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/forExpressionRange.kt");
        }

        @Test
        @TestMetadata("forExpressionVariable.kt")
        public void testForExpressionVariable() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/forExpressionVariable.kt");
        }

        @Test
        @TestMetadata("ifExpression.kt")
        public void testIfExpression() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/ifExpression.kt");
        }

        @Test
        @TestMetadata("intLiteral.kt")
        public void testIntLiteral() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/intLiteral.kt");
        }

        @Test
        @TestMetadata("isExpression.kt")
        public void testIsExpression() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/isExpression.kt");
        }

        @Test
        @TestMetadata("lambdaExpression.kt")
        public void testLambdaExpression() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/lambdaExpression.kt");
        }

        @Test
        @TestMetadata("objectLiteralExpression.kt")
        public void testObjectLiteralExpression() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/objectLiteralExpression.kt");
        }

        @Test
        @TestMetadata("parenthesizedExpression.kt")
        public void testParenthesizedExpression() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/parenthesizedExpression.kt");
        }

        @Test
        @TestMetadata("propertyReferenceExpression.kt")
        public void testPropertyReferenceExpression() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/propertyReferenceExpression.kt");
        }

        @Test
        @TestMetadata("stringLiteral.kt")
        public void testStringLiteral() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/stringLiteral.kt");
        }

        @Test
        @TestMetadata("stringTemplateExpressionEntry.kt")
        public void testStringTemplateExpressionEntry() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/stringTemplateExpressionEntry.kt");
        }

        @Test
        @TestMetadata("throwExpression.kt")
        public void testThrowExpression() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/throwExpression.kt");
        }

        @Test
        @TestMetadata("tryExpression.kt")
        public void testTryExpression() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/tryExpression.kt");
        }

        @Test
        @TestMetadata("unraryExpression.kt")
        public void testUnraryExpression() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/unraryExpression.kt");
        }

        @Test
        @TestMetadata("unraryExpressionOperator.kt")
        public void testUnraryExpressionOperator() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/unraryExpressionOperator.kt");
        }

        @Test
        @TestMetadata("whenExpression.kt")
        public void testWhenExpression() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/whenExpression.kt");
        }

        @Test
        @TestMetadata("whileExpression.kt")
        public void testWhileExpression() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/whileExpression.kt");
        }

        @Test
        @TestMetadata("wholeStringTemplate.kt")
        public void testWholeStringTemplate() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/expressions/wholeStringTemplate.kt");
        }
    }

    @Nested
    @TestMetadata("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/inImport")
    @TestDataPath("$PROJECT_ROOT")
    public class InImport {
        @Test
        public void testAllFilesPresentInInImport() throws Exception {
            KtTestUtil.assertAllTestsPresentByMetadataWithExcluded(this.getClass(), new File("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/inImport"), Pattern.compile("^(.+)\\.kt$"), null, true);
        }

        @Test
        @TestMetadata("firstImportNamePart.kt")
        public void testFirstImportNamePart() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/inImport/firstImportNamePart.kt");
        }

        @Test
        @TestMetadata("importList.kt")
        public void testImportList() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/inImport/importList.kt");
        }

        @Test
        @TestMetadata("middleImportNamePart.kt")
        public void testMiddleImportNamePart() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/inImport/middleImportNamePart.kt");
        }

        @Test
        @TestMetadata("qualifiedImportNamePart.kt")
        public void testQualifiedImportNamePart() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/inImport/qualifiedImportNamePart.kt");
        }

        @Test
        @TestMetadata("wholeImportDirective.kt")
        public void testWholeImportDirective() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/inImport/wholeImportDirective.kt");
        }

        @Test
        @TestMetadata("wholeImportName.kt")
        public void testWholeImportName() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/inImport/wholeImportName.kt");
        }
    }

    @Nested
    @TestMetadata("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/inPackage")
    @TestDataPath("$PROJECT_ROOT")
    public class InPackage {
        @Test
        public void testAllFilesPresentInInPackage() throws Exception {
            KtTestUtil.assertAllTestsPresentByMetadataWithExcluded(this.getClass(), new File("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/inPackage"), Pattern.compile("^(.+)\\.kt$"), null, true);
        }

        @Test
        @TestMetadata("firstPackageNamePart.kt")
        public void testFirstPackageNamePart() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/inPackage/firstPackageNamePart.kt");
        }

        @Test
        @TestMetadata("middlePackageNamePart.kt")
        public void testMiddlePackageNamePart() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/inPackage/middlePackageNamePart.kt");
        }

        @Test
        @TestMetadata("qualifiedPackageNamePart.kt")
        public void testQualifiedPackageNamePart() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/inPackage/qualifiedPackageNamePart.kt");
        }

        @Test
        @TestMetadata("wholePackageDirective.kt")
        public void testWholePackageDirective() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/inPackage/wholePackageDirective.kt");
        }

        @Test
        @TestMetadata("wholePackageName.kt")
        public void testWholePackageName() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/inPackage/wholePackageName.kt");
        }
    }

    @Nested
    @TestMetadata("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/qualifiedExpressions")
    @TestDataPath("$PROJECT_ROOT")
    public class QualifiedExpressions {
        @Test
        public void testAllFilesPresentInQualifiedExpressions() throws Exception {
            KtTestUtil.assertAllTestsPresentByMetadataWithExcluded(this.getClass(), new File("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/qualifiedExpressions"), Pattern.compile("^(.+)\\.kt$"), null, true);
        }

        @Test
        @TestMetadata("firstPartOfQualifiedCallWithNestedClasses.kt")
        public void testFirstPartOfQualifiedCallWithNestedClasses() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/qualifiedExpressions/firstPartOfQualifiedCallWithNestedClasses.kt");
        }

        @Test
        @TestMetadata("lastPartOfQualifiedCallWithNestedClasses.kt")
        public void testLastPartOfQualifiedCallWithNestedClasses() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/qualifiedExpressions/lastPartOfQualifiedCallWithNestedClasses.kt");
        }

        @Test
        @TestMetadata("middlePartOfQualifiedCallWithNestedClasses.kt")
        public void testMiddlePartOfQualifiedCallWithNestedClasses() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/qualifiedExpressions/middlePartOfQualifiedCallWithNestedClasses.kt");
        }

        @Test
        @TestMetadata("qualifiedPartOfQualifiedCallWithNestedClasses.kt")
        public void testQualifiedPartOfQualifiedCallWithNestedClasses() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/qualifiedExpressions/qualifiedPartOfQualifiedCallWithNestedClasses.kt");
        }
    }

    @Nested
    @TestMetadata("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/types")
    @TestDataPath("$PROJECT_ROOT")
    public class Types {
        @Test
        public void testAllFilesPresentInTypes() throws Exception {
            KtTestUtil.assertAllTestsPresentByMetadataWithExcluded(this.getClass(), new File("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/types"), Pattern.compile("^(.+)\\.kt$"), null, true);
        }

        @Test
        @TestMetadata("functionalType.kt")
        public void testFunctionalType() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/types/functionalType.kt");
        }

        @Test
        @TestMetadata("functionalTypeArgument.kt")
        public void testFunctionalTypeArgument() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/types/functionalTypeArgument.kt");
        }

        @Test
        @TestMetadata("invalidTypeArgumentsCount.kt")
        public void testInvalidTypeArgumentsCount() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/types/invalidTypeArgumentsCount.kt");
        }

        @Test
        @TestMetadata("invalidTypeArgumentsCountArgument.kt")
        public void testInvalidTypeArgumentsCountArgument() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/types/invalidTypeArgumentsCountArgument.kt");
        }

        @Test
        @TestMetadata("invalidTypeArgumentsCountFirstArgument.kt")
        public void testInvalidTypeArgumentsCountFirstArgument() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/types/invalidTypeArgumentsCountFirstArgument.kt");
        }

        @Test
        @TestMetadata("invalidTypeArgumentsCountLastArgument.kt")
        public void testInvalidTypeArgumentsCountLastArgument() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/types/invalidTypeArgumentsCountLastArgument.kt");
        }

        @Test
        @TestMetadata("nestedTypeArgument.kt")
        public void testNestedTypeArgument() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/types/nestedTypeArgument.kt");
        }

        @Test
        @TestMetadata("nullableType.kt")
        public void testNullableType() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/types/nullableType.kt");
        }

        @Test
        @TestMetadata("nullableTypeWithooutQuestionMark.kt")
        public void testNullableTypeWithooutQuestionMark() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/types/nullableTypeWithooutQuestionMark.kt");
        }

        @Test
        @TestMetadata("typeArgument.kt")
        public void testTypeArgument() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/types/typeArgument.kt");
        }

        @Test
        @TestMetadata("unresolvedTypeArgumentResolvedTypeConsturctor.kt")
        public void testUnresolvedTypeArgumentResolvedTypeConsturctor() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/types/unresolvedTypeArgumentResolvedTypeConsturctor.kt");
        }

        @Test
        @TestMetadata("unresolvedTypeConsturctorResolvedNestedTypeArgument.kt")
        public void testUnresolvedTypeConsturctorResolvedNestedTypeArgument() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/types/unresolvedTypeConsturctorResolvedNestedTypeArgument.kt");
        }

        @Test
        @TestMetadata("unresolvedTypeConsturctorResolvedTypeArgument.kt")
        public void testUnresolvedTypeConsturctorResolvedTypeArgument() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/types/unresolvedTypeConsturctorResolvedTypeArgument.kt");
        }

        @Test
        @TestMetadata("wholeType.kt")
        public void testWholeType() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/types/wholeType.kt");
        }
    }

    @Nested
    @TestMetadata("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/wholeDeclaration")
    @TestDataPath("$PROJECT_ROOT")
    public class WholeDeclaration {
        @Test
        public void testAllFilesPresentInWholeDeclaration() throws Exception {
            KtTestUtil.assertAllTestsPresentByMetadataWithExcluded(this.getClass(), new File("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/wholeDeclaration"), Pattern.compile("^(.+)\\.kt$"), null, true);
        }

        @Test
        @TestMetadata("classTypeParemeter.kt")
        public void testClassTypeParemeter() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/wholeDeclaration/classTypeParemeter.kt");
        }

        @Test
        @TestMetadata("enumEntry.kt")
        public void testEnumEntry() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/wholeDeclaration/enumEntry.kt");
        }

        @Test
        @TestMetadata("functionTypeParemeter.kt")
        public void testFunctionTypeParemeter() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/wholeDeclaration/functionTypeParemeter.kt");
        }

        @Test
        @TestMetadata("functionValueParameter.kt")
        public void testFunctionValueParameter() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/wholeDeclaration/functionValueParameter.kt");
        }

        @Test
        @TestMetadata("getter.kt")
        public void testGetter() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/wholeDeclaration/getter.kt");
        }

        @Test
        @TestMetadata("localClass.kt")
        public void testLocalClass() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/wholeDeclaration/localClass.kt");
        }

        @Test
        @TestMetadata("localFunction.kt")
        public void testLocalFunction() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/wholeDeclaration/localFunction.kt");
        }

        @Test
        @TestMetadata("localProperty.kt")
        public void testLocalProperty() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/wholeDeclaration/localProperty.kt");
        }

        @Test
        @TestMetadata("memberFunction.kt")
        public void testMemberFunction() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/wholeDeclaration/memberFunction.kt");
        }

        @Test
        @TestMetadata("memberProperty.kt")
        public void testMemberProperty() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/wholeDeclaration/memberProperty.kt");
        }

        @Test
        @TestMetadata("memberTypeAlias.kt")
        public void testMemberTypeAlias() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/wholeDeclaration/memberTypeAlias.kt");
        }

        @Test
        @TestMetadata("nestedClass.kt")
        public void testNestedClass() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/wholeDeclaration/nestedClass.kt");
        }

        @Test
        @TestMetadata("primaryConstructorValValueParameter.kt")
        public void testPrimaryConstructorValValueParameter() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/wholeDeclaration/primaryConstructorValValueParameter.kt");
        }

        @Test
        @TestMetadata("primaryConstructorValueParameter.kt")
        public void testPrimaryConstructorValueParameter() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/wholeDeclaration/primaryConstructorValueParameter.kt");
        }

        @Test
        @TestMetadata("secondaryConstructorValueParameter.kt")
        public void testSecondaryConstructorValueParameter() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/wholeDeclaration/secondaryConstructorValueParameter.kt");
        }

        @Test
        @TestMetadata("setter.kt")
        public void testSetter() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/wholeDeclaration/setter.kt");
        }

        @Test
        @TestMetadata("topLevelClass.kt")
        public void testTopLevelClass() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/wholeDeclaration/topLevelClass.kt");
        }

        @Test
        @TestMetadata("topLevelFunction.kt")
        public void testTopLevelFunction() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/wholeDeclaration/topLevelFunction.kt");
        }

        @Test
        @TestMetadata("topLevelProperty.kt")
        public void testTopLevelProperty() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/wholeDeclaration/topLevelProperty.kt");
        }

        @Test
        @TestMetadata("topLevelTypelTypeAlias.kt")
        public void testTopLevelTypelTypeAlias() throws Exception {
            runTest("idea/idea-frontend-fir/idea-fir-low-level-api/testdata/getOrBuildFir/wholeDeclaration/topLevelTypelTypeAlias.kt");
        }
    }
}
