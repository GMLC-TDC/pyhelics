# -*- coding: utf-8 -*-
# Copyright (c) 2017-2026,
# Battelle Memorial Institute; Lawrence Livermore National Security, LLC; Alliance for Energy
# Innovation LLC. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause

import sys
import os
import shutil


def main(platform_name):
    print(platform_name)
    root = "./dist"
    for file in os.listdir(root):
        if platform_name.replace(".", "_") in file:
            new_file = file.replace(platform_name.replace(".", "_"), platform_name)
            shutil.move(os.path.join(root, file), os.path.join(root, new_file))


if __name__ == "__main__":
    main(sys.argv[1])
