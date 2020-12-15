{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "userDefFunc.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMqSvAeqRht5Pi+VxWL80zf",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/achrisk/Dissertation/blob/main/userDefFunc.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NhUq4IgF8EJk"
      },
      "source": [
        "def my_function(X1,X2):\r\n",
        "\r\n",
        "  R1 = (np.matmul(X1,X1.transpose()))/np.trace(np.matmul(X1,X1.transpose()))\r\n",
        "  R2 = (np.matmul(X2,X2.transpose()))/np.trace(np.matmul(X2,X2.transpose()))\r\n",
        "\r\n",
        "  R = R1+R2\r\n",
        "\r\n",
        "  EValsum, EVecsum = LA.eig(R)\r\n",
        "\r\n",
        "  ind = np.argsort(EValsum)\r\n",
        "  ind = ind[::-1]\r\n",
        "  EVecsum = EVecsum[:,ind]\r\n",
        "  EValsum = EValsum[ind]\r\n",
        "  EValsum = np.diag(EValsum)\r\n",
        "\r\n",
        "  temp=np.transpose(EVecsum)\r\n",
        "  P=np.matmul(sqrtm(inv(EValsum)),temp)\r\n",
        "\r\n",
        "  S1=np.matmul(np.matmul(P,R1),np.transpose(P))\r\n",
        "  S2=np.matmul(np.matmul(P,R2),np.transpose(P))\r\n",
        "\r\n",
        "  w, vr=linalg.eig(S1, S2, False, True)\r\n",
        "  ind = np.argsort(w.real)\r\n",
        "  U = vr[:,ind]\r\n",
        "\r\n",
        "\r\n",
        "\r\n",
        "  result = np.matmul(np.transpose(U),P)\r\n",
        "\r\n",
        "  return result\r\n",
        "\r\n",
        "\r\n",
        "def f_logVar(X):\r\n",
        "\r\n",
        "  X_var = np.var(X,1,ddof=0)\r\n",
        "  X_var_sum = np.sum(X_var)\r\n",
        "  XLog = np.log(np.divide(X_var, X_var_sum))\r\n",
        "\r\n",
        "  return XLog"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
