#!/usr/bin/env python3
"""
Script para convertir imágenes JPG, JPEG y PNG a formato WebP
Mantiene la estructura de directorios y permite configurar la calidad de compresión
"""

import os
import sys
from PIL import Image
import argparse
from pathlib import Path

def convert_image_to_webp(input_path, output_path, quality=85, lossless=False):
    """
    Convierte una imagen a formato WebP
    
    Args:
        input_path (str): Ruta de la imagen original
        output_path (str): Ruta donde guardar la imagen WebP
        quality (int): Calidad de compresión (1-100, solo para lossy)
        lossless (bool): Si usar compresión sin pérdida
    """
    try:
        with Image.open(input_path) as img:
            # Convertir RGBA a RGB si es necesario para JPG
            if img.mode in ('RGBA', 'LA'):
                # Crear fondo blanco
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'RGBA':
                    background.paste(img, mask=img.split()[-1])  # Usar canal alpha como máscara
                else:
                    background.paste(img)
                img = background
            
            # Crear directorio de salida si no existe
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Guardar como WebP
            if lossless:
                img.save(output_path, 'WebP', lossless=True)
            else:
                img.save(output_path, 'WebP', quality=quality, optimize=True)
            
            return True
    except Exception as e:
        print(f"Error convirtiendo {input_path}: {e}")
        return False

def get_webp_filename(original_path):
    """Genera el nombre del archivo WebP basado en el original"""
    path = Path(original_path)
    return path.with_suffix('.webp')

def scan_and_convert_images(source_dir, target_dir=None, quality=85, lossless=False, 
                          extensions=None, backup=False, overwrite=False):
    """
    Escanea un directorio y convierte todas las imágenes encontradas
    
    Args:
        source_dir (str): Directorio fuente
        target_dir (str): Directorio destino (None para convertir in-place)
        quality (int): Calidad de compresión
        lossless (bool): Compresión sin pérdida
        extensions (list): Extensiones a procesar
        backup (bool): Crear backup de originales
        overwrite (bool): Sobrescribir archivos WebP existentes
    """
    if extensions is None:
        extensions = ['.jpg', '.jpeg', '.png']
    
    source_path = Path(source_dir)
    if not source_path.exists():
        print(f"Error: El directorio {source_dir} no existe")
        return
    
    # Estadísticas
    converted = 0
    skipped = 0
    errors = 0
    
    print(f"Escaneando directorio: {source_dir}")
    print(f"Extensiones a procesar: {extensions}")
    print(f"Calidad: {quality}{'% (lossless)' if lossless else '%'}")
    print("-" * 50)
    
    # Buscar todas las imágenes
    for ext in extensions:
        pattern = f"**/*{ext}"
        for img_file in source_path.rglob(pattern):
            if img_file.is_file():
                # Determinar ruta de salida
                if target_dir:
                    # Mantener estructura de directorios en target_dir
                    rel_path = img_file.relative_to(source_path)
                    output_path = Path(target_dir) / rel_path.with_suffix('.webp')
                else:
                    # Convertir in-place
                    output_path = img_file.with_suffix('.webp')
                
                # Verificar si ya existe
                if output_path.exists() and not overwrite:
                    print(f"⏭️  Saltando (ya existe): {img_file.name}")
                    skipped += 1
                    continue
                
                # Crear backup si se solicita
                if backup and not target_dir:
                    backup_path = img_file.with_suffix(f"{img_file.suffix}.backup")
                    if not backup_path.exists():
                        img_file.rename(backup_path)
                
                # Convertir imagen
                print(f"🔄 Convirtiendo: {img_file.name} -> {output_path.name}")
                
                if convert_image_to_webp(str(img_file), str(output_path), quality, lossless):
                    converted += 1
                    
                    # Mostrar información de tamaño
                    original_size = img_file.stat().st_size
                    new_size = output_path.stat().st_size
                    reduction = ((original_size - new_size) / original_size) * 100
                    
                    print(f"   ✅ {original_size:,} bytes -> {new_size:,} bytes "
                          f"({reduction:.1f}% reducción)")
                    
                    # Eliminar original si no hay target_dir y no hay backup
                    if not target_dir and not backup:
                        img_file.unlink()
                        
                else:
                    errors += 1
    
    # Resumen
    print("-" * 50)
    print(f"📊 Resumen:")
    print(f"   ✅ Convertidas: {converted}")
    print(f"   ⏭️  Saltadas: {skipped}")
    print(f"   ❌ Errores: {errors}")

def main():
    parser = argparse.ArgumentParser(description="Convierte imágenes JPG/PNG a WebP")
    parser.add_argument("source", help="Directorio fuente con las imágenes")
    parser.add_argument("-t", "--target", help="Directorio destino (opcional)")
    parser.add_argument("-q", "--quality", type=int, default=85, 
                       help="Calidad de compresión (1-100, default: 85)")
    parser.add_argument("-l", "--lossless", action="store_true",
                       help="Usar compresión sin pérdida")
    parser.add_argument("-e", "--extensions", nargs="+", 
                       default=[".jpg", ".jpeg", ".png"],
                       help="Extensiones a procesar")
    parser.add_argument("-b", "--backup", action="store_true",
                       help="Crear backup de archivos originales")
    parser.add_argument("-o", "--overwrite", action="store_true",
                       help="Sobrescribir archivos WebP existentes")
    
    args = parser.parse_args()
    
    # Validar calidad
    if not 1 <= args.quality <= 100:
        print("Error: La calidad debe estar entre 1 y 100")
        sys.exit(1)
    
    # Normalizar extensiones
    extensions = [ext.lower() if ext.startswith('.') else f'.{ext.lower()}' 
                  for ext in args.extensions]
    
    scan_and_convert_images(
        source_dir=args.source,
        target_dir=args.target,
        quality=args.quality,
        lossless=args.lossless,
        extensions=extensions,
        backup=args.backup,
        overwrite=args.overwrite
    )

if __name__ == "__main__":
    main()
