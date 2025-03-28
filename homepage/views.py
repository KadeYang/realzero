from django.shortcuts import render, get_object_or_404
from .models import Zero_Product
from django.db.models import Q

def index(request):
    return render(request, 'homepage/index.html')

def ranking(request):
    return render(request, 'homepage/ranking.html')

def community(request):
    return render(request, 'homepage/community.html')


def search(request):
    query = request.GET.get('q', '')  # 검색어 가져오기
    print("검색어:", query)
    results = []

    if query:
        results = Zero_Product.objects.filter(
            Q(product_name__icontains=query) |
            Q(Manufacturer__icontains=query)
        )
        print("검색 결과 수:", results.count())

    return render(request, 'homepage/search_results.html', {
        'query': query,
        'results': results,
        'count': results.count()
    })

def product_detail(request, id):
    # 제품 정보를 ID로 조회, 없으면 404 오류 발생
    product = get_object_or_404(Zero_Product, id=id)

    # 말티톨 경고 체크 (원재료명 기준)
    warning = None
    raw_materials = product.Raw_materials.lower() if product.Raw_materials else ""
    if "말티톨" in raw_materials or "maltitol" in raw_materials:
        warning = "⚠️ 경고: 이 제품에는 말티톨이 포함되어 있습니다! 당뇨환자는 말티톨 섭취 시 혈당이 상승할 수 있으므로 주의가 필요합니다."

    # 쉼표 기준으로 원재료 split
    materials_list = [item.strip() for item in product.Raw_materials.split(',') if item.strip()]

    # ✅ 혈당 주의 성분 포함 여부 count
    warning_fields = [
        product.maltitol,
        product.maltitol_syrup,
        product.glucose_syrup,
        product.Sugar_alcohol
    ]
    warnings_count = sum(1 for item in warning_fields if item and item.strip() != '0' and item.strip().lower() != 'null')

    return render(request, 'homepage/product_detail.html', {
        'product': product,
        'warning': warning,
        'materials_list': materials_list,
        'warnings_count': warnings_count,  # 👉 템플릿에서 사용할 수 있게 추가
    })
