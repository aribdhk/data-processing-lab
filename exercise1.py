{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPoknmDsL/DqvtNBvsfvbCj",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/aribdhk/data-processing-lab/blob/main/exercise1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yg_iykz2DM_c",
        "outputId": "5ffc2d5e-0720-4240-bc49-e3c070a55b67"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter student name: ARIB\n",
            "Enter marks for course 1 (0-100): 67\n",
            "Enter marks for course 2 (0-100): 34\n",
            "Enter marks for course 3 (0-100): 99\n",
            "Enter marks for course 4 (0-100): 67\n",
            "Enter marks for course 5 (0-100): 98\n",
            "\n",
            "Student: ARIB\n",
            "Total: 365.0\n",
            "Average: 73.0\n",
            "Highest: 99.0\n",
            "Lowest: 34.0\n",
            "Courses passed: 4 of 5\n",
            "Performance: Good\n"
          ]
        }
      ],
      "source": [
        "PASS_MARK = 50\n",
        "NUM_COURSES = 5\n",
        "\n",
        "name = input(\"Enter student name: \")\n",
        "\n",
        "total = 0\n",
        "highest = 0\n",
        "lowest = 100\n",
        "passed = 0\n",
        "\n",
        "for course_number in range(1, NUM_COURSES + 1):\n",
        "    mark = float(input(\"Enter marks for course \" + str(course_number) + \" (0-100): \"))\n",
        "    while mark < 0 or mark > 100:\n",
        "        print(\"Marks must be between 0 and 100.\")\n",
        "        mark = float(input(\"Enter marks for course \" + str(course_number) + \" (0-100): \"))\n",
        "\n",
        "    total += mark\n",
        "    if mark > highest:\n",
        "        highest = mark\n",
        "    if mark < lowest:\n",
        "        lowest = mark\n",
        "    if mark >= PASS_MARK:\n",
        "        passed += 1\n",
        "\n",
        "average = total / NUM_COURSES\n",
        "\n",
        "if average >= 80:\n",
        "    performance = \"Excellent\"\n",
        "elif average >= 70:\n",
        "    performance = \"Good\"\n",
        "elif average >= 60:\n",
        "    performance = \"Satisfactory\"\n",
        "elif average >= 50:\n",
        "    performance = \"Pass\"\n",
        "else:\n",
        "    performance = \"Needs Improvement\"\n",
        "\n",
        "print()\n",
        "print(\"Student:\", name)\n",
        "print(\"Total:\", round(total, 2))\n",
        "print(\"Average:\", round(average, 2))\n",
        "print(\"Highest:\", highest)\n",
        "print(\"Lowest:\", lowest)\n",
        "print(\"Courses passed:\", passed, \"of\", NUM_COURSES)\n",
        "print(\"Performance:\", performance)"
      ]
    }
  ]
}