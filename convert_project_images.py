#!/usr/bin/env python3
"""
Script simple para convertir imágenes del proyecto UBO-WEB-DTI a WebP
"""

import os
from PIL import Image
from pathlib import Path

def convert_to_webp(input_path, quality=85):
    """Convierte una imagen a WebP manteniendo el mismo nombre y ubicación"""
    try:
        output_path = input_path.with_suffix('.webp')
        
        # Si ya existe WebP, saltar
        if output_path.exists():
            print(f"⏭️  Ya existe: {output_path.name}")
            return False
            
        with Image.open(input_path) as img:
            # Convertir RGBA a RGB si es necesario
            if img.mode in ('RGBA', 'LA'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'RGBA':
                    background.paste(img, mask=img.split()[-1])
                else:
                    background.paste(img)
                img = background
            
            # Guardar como WebP
            img.save(output_path, 'WebP', quality=quality, optimize=True)
            
            # Mostrar estadísticas
            original_size = input_path.stat().st_size
            new_size = output_path.stat().st_size
            reduction = ((original_size - new_size) / original_size) * 100
            
            print(f"✅ {input_path.name} -> {output_path.name}")
            print(f"   📊 {original_size:,} bytes -> {new_size:,} bytes ({reduction:.1f}% reducción)")
            
            return True
            
    except Exception as e:
        print(f"❌ Error con {input_path.name}: {e}")
        return False

def main():
    # Directorios del proyecto
    project_root = Path(__file__).parent
    img_dirs = [
        project_root / "public" / "img",
        project_root / "src" / "assets" / "images"  # por si tienes imágenes aquí también
    ]
    
    # Extensiones a convertir
    extensions = ['.jpg', '.jpeg', '.png']
    
    converted = 0
    total_found = 0
    
    print("🚀 Iniciando conversión de imágenes a WebP")
    print("=" * 50)
    
    for img_dir in img_dirs:
        if not img_dir.exists():
            print(f"📁 Directorio no encontrado: {img_dir}")
            continue
            
        print(f"\n📁 Procesando: {img_dir}")
        
        # Buscar todas las imágenes
        for ext in extensions:
            pattern = f"**/*{ext}"
            for img_file in img_dir.rglob(pattern):
                if img_file.is_file():
                    total_found += 1
                    if convert_to_webp(img_file):
                        converted += 1
    
    print("\n" + "=" * 50)
    print(f"📊 RESUMEN:")
    print(f"   🔍 Imágenes encontradas: {total_found}")
    print(f"   ✅ Convertidas: {converted}")
    print(f"   ⏭️  Saltadas: {total_found - converted}")
    
    if converted > 0:
        print(f"\n💡 Las imágenes WebP están listas para usar!")
        print(f"   Puedes actualizar las referencias en tu código para usar .webp")

if __name__ == "__main__":
    main()
