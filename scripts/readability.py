#!/usr/bin/env python3
"""
readability.py
가독성 분석 스크립트
"""

import sys
import re
from pathlib import Path
from collections import Counter

def analyze_readability(content):
    """가독성 분석"""
    # 문장 분리
    sentences = re.split(r'[.!?]\s+', content)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # 단어 분리 (공백 기준)
    words = content.split()
    
    # 통계
    stats = {
        'total_chars': len(content),
        'total_sentences': len(sentences),
        'total_words': len(words),
        'avg_sentence_length': len(words) / len(sentences) if sentences else 0,
    }
    
    # 표현 반복 체크
    word_counts = Counter(words)
    repeated_words = [(word, count) for word, count in word_counts.most_common(20)
                      if count > 5 and len(word) > 1]
    
    return stats, repeated_words

def main():
    if len(sys.argv) < 2:
        print("Usage: readability.py <file>")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    
    if not file_path.exists():
        print(f"❌ 파일 없음: {file_path}")
        sys.exit(1)
    
    print(f"📊 가독성 분석: {file_path.name}")
    
    content = file_path.read_text(encoding='utf-8')
    stats, repeated = analyze_readability(content)
    
    print(f"   총 글자 수: {stats['total_chars']:,}")
    print(f"   문장 수: {stats['total_sentences']}")
    print(f"   평균 문장 길이: {stats['avg_sentence_length']:.1f}단어")
    
    if repeated:
        print(f"\n⚠️  반복 표현 ({len(repeated)}개):")
        for word, count in repeated[:5]:
            print(f"   '{word}': {count}회")

if __name__ == "__main__":
    main()
