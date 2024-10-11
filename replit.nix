{ pkgs }: {
  deps = [
    pkgs.python39Full  # ระบุ Python เวอร์ชัน 3.10
    pkgs.pip
    pkgs.python39Packages.firebase_admin  # ติดตั้ง firebase_admin
    pkgs.python39Packages.flask           # ติดตั้ง Flask
    pkgs.python39Packages.pillow          # ติดตั้ง Pillow
  ];
}